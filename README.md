### Visually

Python REST API (built with the [*Django Rest Framework*](https://www.django-rest-framework.org))

*Pre-requisites: Anaconda && Conda*

---

##### Project Setup

1. Create virtualenv from environment.yml file `conda create -n visually -f environment.yml`
2. Activate new env `conda activate visually` or `source activate visually` [ OSX - Linux ] or `activate visually` [ Windows ]
3. Clone Project `git clone https://github.com/denyoe/visually.git` && Move into project directory
4. Run the server `python manage.py runserver`
5. Open Browser at `http://127.0.0.1:8000/`

conda install to install packages

---

##### Installing New Packages

Run: `conda install <package name>`

---

##### Freeze Project Requirements

Run: `conda list > environment.yml`