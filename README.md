<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">Data Pirates Challenge - Correios</h3>

  <p align="center">
    Project developed for the crawling challenge for NeoWay job position as Data Analyst.
    <br />
    <a href="https://github.com/lircabin/data-pirates-test"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/lircabin/data-pirates-test/issues">Report Bug</a>
    <a href="https://github.com/lircabin/data-pirates-test/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#tldr">TL;DR</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![Product Name Screen Shot][product-screenshot]

The challenge to be performed was to simply scrape data from the correio's website.

But sometimes data requires visualization.

This project has two parts, one is the crawller, located in the scrapper folder.

The other portion is a web stack for ETLs and Data visualization using a  docker-compose.yml and Dockerfile files, both of which generates a stack for ETL Management (AirFlow), Data Visualization (Grafana) and Database (Postgres). I know this stack is overkill for the task that was given, but I really wanted to build something solid that illustrates a flow for ETLs.

Here's why:
* Scrapping is always only one part of the workflow.
* Data visualization provides insights, tell a story.
* Because it's fun to build stuff :smile:

Of course, in this ReadMe I provide screenshots of the solution running and all files to rebuild it are included, but, if it's only necessary to run the scrapper and check the jsonl file, you can go ahead to <li><a href="#tldr">TL;DR</a></li>


### Built With

* [![Python.py][Python]][Python-url]
* [![Docker.com][Docker]][Docker-url]
* [![Airflow.com][Airflow]][Airflow-url]
* [![Grafana.com][Grafana]][Grafana-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Let's get you setup first: Clone this project to your machine.

### Prerequisites

The requirements are located in the requirements.txt file inside the scrapper folder.

You can either setup a new python environment using or use your current environment.

Just make sure you are running Python 3.8+.

cd into the cloned repository folder and:

* ``` sh
  python -m venv env  && source env/bin/activate 
  ```
* ``` sh
  cd scrapper && pip install -r requirements.txt
  ```

If you want to startup the docker containers go to the root directory of the cloned repository and 

* ``` sh
  docker-compose build && docker-compose up -d 
  ```

The passwords were hardcoded, in case you need to change this, check the docker-compose.yml file and change the environment variables.

Passwords:

*Airflow:
user: airflow
password: airflow

*Grafana:
user: admin
password: admin


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage

Once in the scrapper folder and after installing all required packages you can run tests using pytest:
``` sh
  pytest .
  ```

You can run the python script file with no arguments, but you can also define if you want to scrape a specific set (comma separated values) of UFs:

``` sh
  python3 .
```

or

``` sh
  python3 . --ufs=BA,SP,MG
```

To use the docker container and have the ETL and Data Visualization capabilities, after building and starting the container, you can go to:

* Airflow: http://localhost:8000/
* Grafana: http://localhost:8080/

In Grafana there should be a dashboard named "Dashboard Brazilian Cities" to view data from.

Check if the Airflow dag is running and has completed before you hit refresh in Grafana's dashboard view otherwise, since no volume was assigned to postgres, there will be no data as postgres database is empty.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## TLDR

Create a new python environment and activate it:
``` sh
  python -m venv env  && source env/bin/activate 
```
Get into the scrapper folder:
``` sh
  cd scrapper
```
Run the scrapper:
``` sh
  python3 . 
```

Profit

<!-- ROADMAP -->
## Roadmap

- [x] Create ReadMe
- [x] Build Tests
- [x] Build scripts to solve testing
- [x] Check if files are being created
- [x] Create Docker File and Docker-compose environment
- [x] Create DAG
- [x] Create ETL scripts
- [x] Create Grafana Dashboard

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Matheus Alves - [@okmatheusalves](https://linkedin.com/in/okmatheusalves) - alves@lircabin.com

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/lircabin/data-pirates-neoway.svg?style=for-the-badge
[contributors-url]: https://github.com/lircabin/data-pirates-neoway/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/lircabin/data-pirates-neoway.svg?style=for-the-badge
[forks-url]: https://github.com/lircabin/data-pirates-neoway/network/members
[stars-shield]: https://img.shields.io/github/stars/lircabin/data-pirates-neoway?style=for-the-badge
[stars-url]: https://github.com/lircabin/data-pirates-neoway/stargazers
[issues-shield]: https://img.shields.io/github/issues/lircabin/data-pirates-neoway?style=for-the-badge
[issues-url]: https://github.com/lircabin/data-pirates-neoway/issues
[license-shield]: https://img.shields.io/github/license/lircabin/data-pirates-neoway.svg?style=for-the-badge
[license-url]: https://github.com/lircabin/data-pirates-neoway/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/okmatheusalves
[product-screenshot]: images/screenshot.png
[Docker]: https://img.shields.io/badge/Docker-0769AD?style=for-the-badge&logo=docker&logoColor=white
[Docker-url]: https://docker.com 
[Python]: https://img.shields.io/badge/Python-0769AD?style=for-the-badge&logo=python&logoColor=yellow
[Docker-url]: https://docker.com 
[Docker]: https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white
[Docker-url]: https://docker.com 
[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://python.org
[Grafana]: https://img.shields.io/badge/Grafana-000000?style=for-the-badge&logo=grafana&logoColor=orange
[Grafana-url]: https://grafana.com/
[Airflow]: https://img.shields.io/badge/Apache%20Airflow-017CEE?style=for-the-badge&logo=Apache%20Airflow&logoColor=white
[Airflow-url]: https://airflow.apache.org/
