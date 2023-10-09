from datetime import datetime

import module_1


def main():
    start_time = datetime.now()
    module_1.do_something(end=100_000_000)
    time_spent = datetime.now() - start_time

    print(f"{time_spent.total_seconds():.2f} seg.")


if __name__ == "__main__":
    main()
    # Terminou em ~18 segundos.
