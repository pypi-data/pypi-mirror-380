#!/usr/bin/env python3
import argparse
import os
import subprocess
import sys
import json
from pathlib import Path
import urllib.parse
import threading
import itertools
import time

# ------------------------
# Helpers
# ------------------------

class Spinner:
    """Simple terminal spinner shown while long-running actions run."""
    def __init__(self, prefix=""):
        self._stop = threading.Event()
        self._pause = threading.Event()
        self._thread = None
        self.prefix = prefix
        self.chars = "|/-\\"

    def _spin(self):
        for c in itertools.cycle(self.chars):
            if self._stop.is_set():
                break
            if self._pause.is_set():
                time.sleep(0.1)
                continue
            sys.stdout.write(f"\r{self.prefix}{c} ")
            sys.stdout.flush()
            time.sleep(0.12)
        # clear spinner
        sys.stdout.write("\r" + " " * (len(self.prefix) + 2) + "\r")
        sys.stdout.flush()

    def start(self):
        if self._thread and self._thread.is_alive():
            return
        self._stop.clear()
        self._pause.clear()
        self._thread = threading.Thread(target=self._spin, daemon=True)
        self._thread.start()

    def stop(self):
        self._stop.set()
        if self._thread:
            self._thread.join()

    def pause(self):
        self._pause.set()

    def resume(self):
        self._pause.clear()


# Emoji helpers
def info(msg):
    print(f"ℹ️  {msg}")


def success(msg):
    print(f"✅  {msg}")


def warn(msg):
    print(f"⚠️  {msg}")


def fail(msg):
    print(f"❌  {msg}")


def print_output(process, title: str = None):
    """
    Stream subprocess output while showing a small spinner and emoji prefixes.
    """
    spinner = Spinner(prefix=(f"{title} " if title else ""))
    spinner.start()
    try:
        for line in process.stdout:
            spinner.pause()
            # prefix streaming lines for readability
            print(f"🔁 {line}", end="", flush=True)
            spinner.resume()
        process.wait()
    finally:
        spinner.stop()

    if process.returncode == 0:
        if title:
            success(f"{title} finished")
        else:
            success("Command finished")
    else:
        if title:
            fail(f"{title} failed (exit {process.returncode})")
        else:
            fail(f"Command failed (exit {process.returncode})")


def check_installation(cmd, install_cmd=None):
    try:
        res = subprocess.run([cmd, "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        success(f"{cmd} is installed ({res.stdout.strip()})")
    except Exception:
        prompt = input(f"❌ {cmd} not found. Install it? (y/n): ").lower()
        if prompt in {"y", "yes"}:
            if not install_cmd:
                fail(f"No install command for {cmd}. Please install manually.")
                sys.exit(1)
            info(f"Installing {cmd}...")
            process = subprocess.Popen(install_cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            print_output(process, title=f"install {cmd}")
            if process.returncode == 0:
                success(f"{cmd} installed successfully!")
            else:
                fail(f"Failed to install {cmd}. Exiting.")
                sys.exit(1)
        else:
            warn(f"Skipping {cmd}. This may cause errors.")


# ------------------------
# Postgres
# ------------------------

def setup_postgres(db_name, db_user, db_pass):
    """Setup PostgreSQL DB and user with CREATEDB privilege for Prisma migrations"""
    info(f"Postgres: creating DB '{db_name}' and user '{db_user}' with CREATEDB privilege...")

    try:
        # 1. Create/alter user
        create_user_sql = f"""
        DO
        $do$
        BEGIN
           IF NOT EXISTS (SELECT FROM pg_catalog.pg_roles WHERE rolname = '{db_user}') THEN
              CREATE ROLE {db_user} LOGIN PASSWORD '{db_pass}' CREATEDB;
           ELSE
              ALTER ROLE {db_user} WITH LOGIN PASSWORD '{db_pass}' CREATEDB;
           END IF;
        END
        $do$;
        """
        subprocess.run(
            ["sudo", "-u", "postgres", "psql", "-v", "ON_ERROR_STOP=1", "-c", create_user_sql],
            check=True
        )

        # 2. Create database (only if missing)
        check_db_sql = f"SELECT 1 FROM pg_database WHERE datname = '{db_name}';"
        result = subprocess.run(
            ["sudo", "-u", "postgres", "psql", "-tAc", check_db_sql],
            capture_output=True, text=True
        )

        if not result.stdout.strip():
            subprocess.run(
                ["sudo", "-u", "postgres", "psql", "-v", "ON_ERROR_STOP=1",
                 "-c", f"CREATE DATABASE {db_name} OWNER {db_user};"],
                check=True
            )
            success(f"Database '{db_name}' created and owned by '{db_user}'.")
        else:
            info(f"Database '{db_name}' already exists. Skipping creation.")

        success(f"Database '{db_name}' and user '{db_user}' ready.")
        print()

    except subprocess.CalledProcessError as e:
        fail(f"PostgreSQL setup failed: {e}")
        sys.exit(1)




# ------------------------
# Project Scaffold
# ------------------------

def create_project_structure(project_name, db_url):
    info(f"Creating project '{project_name}' structure...")
    base = Path(project_name)
    os.makedirs(base / "src" / "routes", exist_ok=True)
    os.makedirs(base / "tests", exist_ok=True)
    os.makedirs(base / "prisma", exist_ok=True)

    (base / ".env").write_text(f'DATABASE_URL="{db_url}"\n')

    # app.js
    (base / "src" / "app.js").write_text(
        """const express = require("express");
const app = express();
app.get("/health", (req, res) => res.json({status: "OK"}));
module.exports = app;
"""
    )

    # server.js
    (base / "server.js").write_text(
        """const app = require("./src/app");
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
"""
    )

    # Prisma schema
    schema_file = base / "prisma" / "schema.prisma"
    if not schema_file.exists():
        schema_file.write_text(
            """generator client {
  provider = "prisma-client-js"
}

datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

model User {
  id    Int     @id @default(autoincrement())
  email String  @unique
  name  String?
}
"""
        )

    # Test file
    (base / "tests" / "app.test.js").write_text(
        """const request = require("supertest");
const app = require("../src/app");
const { PrismaClient } = require("@prisma/client");

const prisma = new PrismaClient();

describe("Health check", () => {
  it("GET /health", async () => {
    const res = await request(app).get("/health");
    expect(res.statusCode).toBe(200);
  });

  it("Database connection", async () => {
    const result = await prisma.$queryRaw`SELECT 1 as number`;
    expect(result[0].number).toBe(1);
  });
});
"""
    )

    success(f"Project structure created at {base}")
    print()


# ------------------------
# Node Setup
# ------------------------

def setup_node_dependencies(project_name):
    os.chdir(project_name)
    info("Installing Node dependencies 📦")
    subprocess.run(["npm", "install", "express", "prisma", "@prisma/client"], check=True)
    subprocess.run(["npm", "install", "--save-dev", "jest", "supertest", "dotenv"], check=True)

    if not Path("prisma").exists():
        subprocess.run(["npx", "prisma", "init"], check=True)
    else:
        warn("Skipping `prisma init` because `prisma/` exists.")

    # Add Jest config
    with open("package.json", "r") as f:
        pkg = json.load(f)
    pkg.setdefault("scripts", {})
    pkg["scripts"]["test"] = "jest"
    pkg["jest"] = {"setupFiles": ["<rootDir>/jest.setup.js"]}
    with open("package.json", "w") as f:
        json.dump(pkg, f, indent=2)

    # jest.setup.js
    (Path("jest.setup.js")).write_text('require("dotenv").config();\n')

    # Run Prisma migrations
    info("Running Prisma migrations 🚀")
    subprocess.run(["npx", "prisma", "migrate", "dev", "--name", "init"], check=True)
    success("Dependencies installed and Prisma migrations applied.")


# ------------------------
# CLI Entry
# ------------------------

def main():
    parser = argparse.ArgumentParser(description="Express + Prisma Bootstrap CLI")
    parser.add_argument("project_name", help="Project name")
    parser.add_argument("--db-name", required=True, help="Database Name")
    parser.add_argument("--db-user", required=True, help="Database User")
    parser.add_argument("--db-pass", required=True, help="Database Password")
    args = parser.parse_args()

    # Dependency checks
    check_installation("node", ["sudo", "apt", "install", "-y", "nodejs", "npm"])
    check_installation("npm", ["sudo", "apt", "install", "-y", "npm"])
    check_installation("psql", ["sudo", "apt", "install", "-y", "postgresql-client"])
    check_installation("prisma", ["sudo", "npm", "install", "-g", "prisma"])
    check_installation("psql", ["sudo", "apt", "install", "-y", "postgresql", "postgresql-contrib"]
)

    # Postgres
    setup_postgres(args.db_name, args.db_user, args.db_pass)

    # Encode password for URL
    password_encoded = urllib.parse.quote(args.db_pass)
    db_url = f"postgresql://{args.db_user}:{password_encoded}@localhost:5432/{args.db_name}?schema=public"

    # Scaffold
    create_project_structure(args.project_name, db_url)

    # Node deps & migrations
    setup_node_dependencies(args.project_name)

    success(f"Project {args.project_name} ready!")
    info("Next steps:")
    print(f"   👉 cd {args.project_name}")
    print(f"   👉 npm test   # run tests")
    print(f"   👉 node server.js   # start server")


if __name__ == "__main__":
    main()
