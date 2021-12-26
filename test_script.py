import os

from django.core.wsgi import get_wsgi_application

# in order to run scripts, environment setup is required
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'personal_portfolio.settings')
application = get_wsgi_application()

from projects.models import Project


def install_project():
    p1 = Project(
        title='My First Project',
        description='A web development project.',
        technology='Django',
        image='img/project1.png'
    )
    p1.save()

    p2 = Project(
        title='My second project',
        description='Another web development project',
        technology='Flask',
        image='img/project2.png'
    )
    p2.save()

    p3 = Project(
        title='My third project',
        description='A final development project',
        technology='Django',
        image='img/project3.png'
    )
    p3.save()

if __name__ == '_main__':
    pass
    # install_project()
