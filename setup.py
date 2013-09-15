#  setuptools file  By Amal

# ---------------------------------

from setuptools import setup , find_packages
setup( name = "mycraaawler",
        version = "0.1",
        packages = find_packages(),
        scripts = ['mycraaawler'],
        install_requires=['BeautifulSoup'],
        package_data = { 'pymycraawler': [''], }, 
        author = "Amal Roumi Suliman",
        author_email = "roumia@gmail.com",
        description = "Web spider ",
        license  = "GNU GPLv3",
        keywords = "web_crawler ,MSWL, web_spider, python ",
        url = "",
        long_description = "Python application Assignments for Development Tools one of the subject in MSWL that"
                           "get the current version of a web pagSpider to track the updates of a web page",
        download_url = "", )
