from VictorOS.core.kernel import Kernel


def main() -> None:
    kernel = Kernel()
    kernel.boot()


if __name__ == "__main__":
    main()