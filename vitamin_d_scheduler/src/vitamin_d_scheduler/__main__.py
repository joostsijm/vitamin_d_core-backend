"""Main application"""

import sys
import time

from vitamin_d_scheduler import create_app


def main():
    """Main function"""
    app = create_app()
    app.run(host='0.0.0.0')
    try:
        while True:
            time.sleep(100)
    except KeyboardInterrupt:
        sys.exit()

if __name__ == '__main__':
    main()
