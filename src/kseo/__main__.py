"""Explicit local operations. JSON output is private unless the user shares it."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import sqlite3
import sys
from . import Store, KSEOError


def main() -> int:
    parser = argparse.ArgumentParser(prog="python -m kseo")
    parser.add_argument("--instance", required=True, help="Private instance directory")
    sub = parser.add_subparsers(dest="command", required=True)
    init = sub.add_parser("init"); init.add_argument("--workspace")
    snap = sub.add_parser("snapshot")
    snap.add_argument("file"); snap.add_argument("--uri", required=True); snap.add_argument("--scope", required=True)
    pack = sub.add_parser("packet")
    pack.add_argument("--question", required=True); pack.add_argument("--purpose", required=True)
    pack.add_argument("--source", action="append", required=True); pack.add_argument("--competence", default="kseo-cognitive-relation")
    response = sub.add_parser("response")
    response.add_argument("packet_id"); response.add_argument("json_file")
    proposal = sub.add_parser("propose")
    proposal.add_argument("target"); proposal.add_argument("replacement_file")
    proposal.add_argument("--reason", required=True); proposal.add_argument("--competence", required=True)
    proposal.add_argument("--response-id")
    apply = sub.add_parser("apply")
    apply.add_argument("proposal_id"); apply.add_argument("--permit", required=True); apply.add_argument("--actor", required=True)
    verify = sub.add_parser("verify"); verify.add_argument("proposal_id")
    read = sub.add_parser("read"); read.add_argument("record_id")
    teach = sub.add_parser("teach"); teach.add_argument("json_file")
    sub.add_parser("status")
    args = parser.parse_args()
    try:
        with (Store.create(args.instance, workspace=args.workspace) if args.command == "init" else Store(args.instance)) as store:
            if args.command in {"init", "status"}:
                result = store.status()
            elif args.command == "snapshot":
                result = store.snapshot(args.file, uri=args.uri, scope=args.scope)
            elif args.command == "packet":
                result = store.packet(question=args.question, purpose=args.purpose, source_ids=args.source, competence=args.competence)
            elif args.command == "response":
                result = store.response(args.packet_id, json.loads(Path(args.json_file).read_text(encoding="utf-8")))
            elif args.command == "propose":
                result = store.propose(args.target, Path(args.replacement_file).read_text(encoding="utf-8"), reason=args.reason,
                                       competence=args.competence, response_id=args.response_id)
            elif args.command == "apply":
                result = store.apply(args.proposal_id, permit=args.permit, actor=args.actor)
            elif args.command == "verify":
                result = store.verify(args.proposal_id)
            elif args.command == "read":
                result = store.get(args.record_id)
            else:
                result = store.teach(**json.loads(Path(args.json_file).read_text(encoding="utf-8")))
            print(json.dumps(result, indent=2, ensure_ascii=False, allow_nan=False))
            return 0
    except (KSEOError, OSError, sqlite3.Error, json.JSONDecodeError, TypeError, UnicodeError) as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
