#! coding: utf-8
"""Simple cli script to get and trigger Jenkins build
"""

import os
import click
import jenkins

J_ID = os.environ['JENKINS_ID']
J_TOKEN = os.environ['JENKINS_TOKEN']
J_ADDR = os.environ['JENKINS_ADDR']
J_URL = 'http://{}:{}@{}'.format(J_ID, J_TOKEN, J_ADDR)

@click.command()
@click.option("-f", "--find", "keyword", type=str, help="find jenkins job with keyword")
@click.option("-b", "--build", "build_name", help="build jenkins job with build_name")
def jenkins_job(keyword, build_name):
    """
    Find and print all Jenkins job that contains keyword
    Trigger Jenkins to build the job with job_name

    Options:
      -f, --find keyword
      -b, --build build_name
    """

    jobs = J_SERVER.get_jobs()
    if keyword:
        for job in jobs:
            job_name = job['name']
            if keyword in job_name:
                click.echo(job_name)
    elif build_name:
        click.echo("Building job {}.".format(build_name))
        output = J_SERVER.build_job(build_name)
        click.echo("Build number {}.".format(output))
        #    click.echo("Job {} not found".format(build_name))

if __name__ == '__main__':
    J_SERVER =  jenkins.Jenkins(J_URL, timeout=5)
    
    # wait for at least 30 seconds for Jenkins to be ready
    if J_SERVER.wait_for_normal_op(30):
            jenkins_job()
    else:
        print("Jenkins failed to be ready in sufficient time")
