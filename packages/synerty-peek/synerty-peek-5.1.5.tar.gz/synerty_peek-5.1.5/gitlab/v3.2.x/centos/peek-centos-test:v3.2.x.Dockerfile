FROM peek-centos:v3.2.x
ENV RELEASE_BRANCH="v3.2.x"

WORKDIR /root

# Download and install the pinned packages for this release
#
RUN wget "https://gitlab.synerty.com/peek/peek/-/raw/${RELEASE_BRANCH}/gitlab/${RELEASE_BRANCH}/centos/pinned-deps-py"
RUN pip install -r pinned-deps-py

# Install the unit test report converters
RUN pip install subunitreporter junitxml ddt
