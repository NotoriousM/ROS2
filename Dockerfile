FROM osrf/ros:jazzy-desktop

SHELL ["/bin/bash", "-c"]

WORKDIR /app

COPY src ws_pub_sub/src

RUN cd ws_pub_sub && \
    source /opt/ros/jazzy/setup.bash && \
    colcon build

COPY entrypoint.sh /

ENTRYPOINT [ "/entrypoint.sh" ]

CMD ["bash"]

