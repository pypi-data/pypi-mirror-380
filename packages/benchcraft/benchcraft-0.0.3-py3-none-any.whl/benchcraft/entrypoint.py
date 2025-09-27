import argparse
import benchcraft


def main():
    parser = argparse.ArgumentParser(
        description="benchcraft - Craft and run benchmarks."
    )

    subparsers = parser.add_subparsers(dest="command")

    server_parser = subparsers.add_parser("serve", help="Start the webserver")
    server_parser.set_defaults(func=benchcraft.server.main)

    # TODO
    # agent_parser = subparsers.add_parser("agent", help="Start the agent")
    # agent_parser.set_defaults(func=benchcraft.agents.main)
    # agent_parser.add_argument(
    #     "--config",
    #     type=str,
    #     default="benchmarks/example_eval.json",
    #     help="Path to the configuration file",
    # )

    args = parser.parse_args()

    if hasattr(args, "func"):
        # if args.func == benchcraft.agent.main:
        #     args.func(args.config)
        # else:
        args.func()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
