import argparse
import sys
from .http import MirDIPClient, DEFAULT_BASE_URL


def _add_common_args(p: argparse.ArgumentParser) -> None:
	p.add_argument("--base-url", default=None, help="Override base URL (default: mirDIP public)")
	p.add_argument("--timeout", type=float, default=60.0, help="Request timeout in seconds")


def cmd_genes(args: argparse.Namespace) -> int:
	client = MirDIPClient(base_url=args.base_url or DEFAULT_BASE_URL, timeout=args.timeout)
	resp = client.search_genes(args.genes, args.score)
	print(resp.results)
	return 0


def cmd_micrornas(args: argparse.Namespace) -> int:
	client = MirDIPClient(base_url=args.base_url or DEFAULT_BASE_URL, timeout=args.timeout)
	resp = client.search_micro_rnas(args.micrornas, args.score)
	print(resp.results)
	return 0


def cmd_bidirectional(args: argparse.Namespace) -> int:
	client = MirDIPClient(base_url=args.base_url or DEFAULT_BASE_URL, timeout=args.timeout)
	resp = client.search_bidirectional(
		args.genes,
		args.micrornas,
		args.score,
		args.sources,
		args.occurrences,
	)
	print(resp.results)
	return 0


def main(argv=None) -> int:
	argv = argv if argv is not None else sys.argv[1:]
	ap = argparse.ArgumentParser(prog="mirdip", description="CLI for mirDIP API")
	sub = ap.add_subparsers(dest="cmd", required=True)

	apg = sub.add_parser("genes", help="Unidirectional search on genes")
	apg.add_argument("genes", help="Comma-delimited gene symbols")
	apg.add_argument("score", choices=["Very High", "High", "Medium", "Low"], help="Minimum score")
	_add_common_args(apg)
	apg.set_defaults(func=cmd_genes)

	apm = sub.add_parser("micrornas", help="Unidirectional search on microRNAs")
	apm.add_argument("micrornas", help="Comma-delimited microRNAs")
	apm.add_argument("score", choices=["Very High", "High", "Medium", "Low"], help="Minimum score")
	_add_common_args(apm)
	apm.set_defaults(func=cmd_micrornas)

	apb = sub.add_parser("bidirectional", help="Bidirectional search")
	apb.add_argument("genes", help="Comma-delimited gene symbols")
	apb.add_argument("micrornas", help="Comma-delimited microRNAs")
	apb.add_argument("score", choices=["Very High", "High", "Medium", "Low"], help="Minimum score")
	apb.add_argument("sources", help="Comma-delimited sources list")
	apb.add_argument("occurrences", help="Minimum number of sources (1-24)")
	_add_common_args(apb)
	apb.set_defaults(func=cmd_bidirectional)

	args = ap.parse_args(argv)
	return args.func(args)


if __name__ == "__main__":
	raise SystemExit(main())

