"""Main application"""

import sys
import time

from vitamin-d-scheduler import create_app


def main():
    """Main function"""
    app = create_app()
    app.run()
    try:
        while True:
            time.sleep(100)
    except KeyboardInterurrupt:
        sys.exit()

if __name__ == '__main__':
    main()
