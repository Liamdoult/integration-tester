from integration_tester import driver, errors

import docker
import pytest 


def test_driver_standard():
    """ Standard driver use test. """
    pull = "ubuntu:latest"
    drive = driver.Driver(pull)
    id = drive._container.id
    assert drive.ready() == True
    assert drive.reset() == True
    assert drive.wait_until_ready(timeout=10) is None
    drive._status = False 
    with pytest.raises(errors.ReadyTimeout):
        drive.wait_until_ready(timeout=2)
    del(drive)
    with pytest.raises(docker.errors.NotFound):
        driver.CLIENT.containers.get(id)
    

def test_image_removal():
    """ Test that we correctly remove the local image.

    This test ensures that a local downloaded image is deleted correctly if
    requested by the client. This feature allows the client to reduce the
    storage overhead of docker.
    """
    pull = "ubuntu:latest"
    drive = driver.Driver(pull, remove_image=True)
    del(drive)
    assert not driver.CLIENT.images.list(pull)
    

