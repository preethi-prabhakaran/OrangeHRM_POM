The OrangeHRM_POM project is a Selenium-based Unittest automation framework for testing key functionalities of the OrangeHRM web application. This framework adheres to the Page Object Model (POM) to promote better test code maintenance and scalability. It provides a solid base for automating repetitive tasks and validating application behavior.

OrangeHRM_POM/
├── config/
│   ├── XPATHs.py             # Stores XPATH locators for web elements
│   └── variables.py          # Stores configurable variables (e.g., URLs, credentials)
├── library/
│   ├── common.py             # Utility functions for repetitive tasks
│   ├── log_config.py         # Logger configuration for test execution
│   └── pages/
│       ├── loginpage.py      # Page object for login functionality
│       ├── buzzpage.py       # Page object for the Buzz tab
│       ├── pimpage.py        # Page object for the PIM tab
│       └── recruitmentpage.py # Page object for the Recruitment tab
├── tests/
│   ├── Buzz.py               # Test cases for the Buzz tab
│   ├── PIM.py                # Test cases for the PIM tab
│   ├── Recruitment.py        # Test cases for the Recruitment tab
│   └── TestSuite_runner.py   # Test suite and runner file
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation

