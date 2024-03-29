from itertools import chain

from wanderu.bamboo.job import Job
from wanderu.bamboo.test.util import random_job_dict

def test_job_serialization():
    jd = random_job_dict()
    job1 = Job.from_dict(jd)
    jd2 = job1.as_dict()
    job2 = Job.from_dict(jd2)

    testkeys = ['id', 'payload', 'priority']

    for k in testkeys:
        assert jd[k] == jd2[k], "Job dict mismatch %s %s" % (jd, jd2)

    assert job1 == job2

    jl = list(chain(*list(jd.items())))
    job2 = Job.from_string_list(jl)
    jl2 = job2.as_string_tup()

    assert all((v in set(jl2) for v in jl))

    for k in testkeys:
        assert getattr(job1, k, "A") == getattr(job2, k, "B")

def test_invalid_job_field():
    jd = random_job_dict()
    job = Job.from_dict(jd)

    try:
        job.notafield = 'not a value'
    except KeyError:
        pass
    else:
        raise Exception("Shit, this was supposed to error.")
