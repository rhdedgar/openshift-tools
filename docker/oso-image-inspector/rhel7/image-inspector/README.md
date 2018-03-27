# Image Inspector

Image Inspector can extract docker images to a target directory and
(optionally) serve the content through webdav.

    $ image-inspector --image=fedora:22 --serve 0.0.0.0:8080 --scan-type=openscap
    2015/12/10 19:24:44 Image fedora:22 is available, skipping image pull
    2015/12/10 19:24:44 Extracting image fedora:22 to
                        /var/tmp/image-inspector-121627917
    2015/12/10 19:24:46 Serving image content
                        /var/tmp/image-inspector-121627917 on
                        webdav://0.0.0.0:8080/api/v1/content/

    $ cadaver http://localhost:8080/api/v1/content
    dav:/api/v1/content/> ls
    Listing collection `/api/v1/content/': succeeded.
    Coll:   boot                                4096  Dec 10 20:24
    Coll:   dev                                 4096  Dec 10 20:24
    Coll:   etc                                 4096  Dec 10 20:24
    Coll:   home                                4096  Dec 10 20:24
    Coll:   lost+found                          4096  Dec 10 20:24
    ...


## OpenSCAP support

Image Inspector can inspect images using OpenSCAP and serve the scan result.
The OpenSCAP scan report will be served on <serve_path>/api/v1/openscap and
the status of the scan will be available on <serve_path>/api/v1/metadata in
the OpenSCAP section.  An HTML OpenSCAP scan report will be served on
<serve_path>/api/v1/openscap-report if the `--openscap-html-report` option is used.

    $ sudo image-inspector --image=fedora:22 --path=/tmp/image-content --scan-type=openscap
			--serve 0.0.0.0:8080 --chroot
    2016/05/25 16:12:04 Image fedora:22 is available, skipping image pull
    2016/05/25 16:12:04 Extracting image fedora:22 to /tmp/image-content
    2016/05/25 16:12:14 OpenSCAP scanning /tmp/image-content. Placing results in /var/tmp/image-inspector-scan-results-845509636
    2016/05/25 16:12:20 Serving image content /tmp/image-content on webdav://0.0.0.0:8080/api/v1/content/

## ClamAV support

Image Inspector can inspect images using ClamAV. To use the ClamAV scan you first
have to install the ClamAV server. To initiate the scan you need to provide location
of the ClamAV socket file using the  `-clam-socket` flag:

    $ sudo image-inspector --image=mfojtik/virus-test:latest --scan-type=clamav --clam-socket=/var/run/clamd.socket
    2017/06/20 19:40:48 Pulling image docker.io/mfojtik/virus-test:latest
    2017/06/20 19:40:51 Extracting image docker.io/mfojtik/virus-test:latest to /var/tmp/image-inspector-992373344
    2017/06/20 19:40:55 clamav scan took 1s (1 problems found)

# Integration with third-party services

To retrieve the compacted scan results, you can provide the `-post-results-url` option
which will cause the Image Inspector to HTTP POST the results in JSON form to the given
URL. To make sure you only process results from the Image Inspector you trust, you can
provide the `-post-results-token-file` option and point it to a file with shared token.

# Building

To build the image-inspector you can run this command:

    $ make

# Running as a container

    $ docker run -ti --rm --privileged -p 8080:8080 \
      -v /var/run/docker.sock:/var/run/docker.sock \
      openshift/image-inspector --image=registry.access.redhat.com/rhel7:latest \
      --path=/tmp/image-content --scan-type=openscap --serve 0.0.0.0:8080
