# exercise 3.4 answers:

In the beginning, my backend and frontend containers sizes were about 1.0 GB per each. After removing extra packages from containers and joining all RUN commands together, I succeeded to reduce image sizes. Frontend size reduced from 1.0 GB to 450.0 MB. Backend size reduced from 1.0 GB to 600.0 MB. New dockerfiles can be found in this folder and older dockerfiles can be found in previous exercise folder.

I also used ubuntu:18.04 image in both frontend and backend. Before I had golang and node images.