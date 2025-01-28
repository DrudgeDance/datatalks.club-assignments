# Answer to Question 01

Simple setup to run Python 3.12.8 in Docker and check pip version.

```bash
cd Week01/Assignment01/Question01
docker build -t python-assignment .
docker run -it python-assignment
pip --version
exit
```

The output of the commands is:
```
adamduda@Adams-MacBook-Pro Assignment01 % docker build -t python-assignment .
[+] Building 14.6s (7/7) FINISHED                                                                              docker:desktop-linux
 => [internal] load build definition from Dockerfile                                                                           0.0s
 => => transferring dockerfile: 128B                                                                                           0.0s
 => [internal] load metadata for docker.io/library/python:3.12.8                                                               1.0s
 => [auth] library/python:pull token for registry-1.docker.io                                                                  0.0s
 => [internal] load .dockerignore                                                                                              0.0s
 => => transferring context: 2B                                                                                                0.0s
 => [1/2] FROM docker.io/library/python:3.12.8@sha256:2e726959b8df5cd9fd95a4cbd6dcd23d8a89e750e9c2c5dc077ba56365c6a925        12.2s
 => => resolve docker.io/library/python:3.12.8@sha256:2e726959b8df5cd9fd95a4cbd6dcd23d8a89e750e9c2c5dc077ba56365c6a925         0.0s
 => => sha256:86f9cc2995adc9ec276a7963ba4592bfddcff8901088fea7907999f5ffce55dc 250B / 250B                                     0.1s
 => => sha256:c80762877ac59b755105fb2ab333f35c02bb8ad616267989de82a6d475daa051 24.87MB / 24.87MB                               0.7s
 => => sha256:c980de82d0336a7869939375b50dc33778de7bcd9640dacbbfa968f71446b3a5 6.24MB / 6.24MB                                 0.7s
 => => sha256:94c5996c7a64a4f64139ff9df6a590216c8143f5bb1f4c0f41874cf5336645c0 202.72MB / 202.72MB                             9.2s
 => => sha256:936252136b926e9bca27f4a5442f6a5d10c0ea4a23ca8b30c65de1bde666d082 64.36MB / 64.36MB                               5.5s
 => => sha256:d22b85d68f8a4dce392d372c8a196863eac6d111c36b714179b4ab30e00c00d1 23.60MB / 23.60MB                               2.2s
 => => sha256:e474a4a4cbbfe5b308416796d99b79605bbfad6cb32ab1d94d61dc0585a907ea 48.31MB / 48.31MB                               4.2s
 => => extracting sha256:e474a4a4cbbfe5b308416796d99b79605bbfad6cb32ab1d94d61dc0585a907ea                                      0.9s
 => => extracting sha256:d22b85d68f8a4dce392d372c8a196863eac6d111c36b714179b4ab30e00c00d1                                      0.3s
 => => extracting sha256:936252136b926e9bca27f4a5442f6a5d10c0ea4a23ca8b30c65de1bde666d082                                      1.0s
 => => extracting sha256:94c5996c7a64a4f64139ff9df6a590216c8143f5bb1f4c0f41874cf5336645c0                                      2.5s
 => => extracting sha256:c980de82d0336a7869939375b50dc33778de7bcd9640dacbbfa968f71446b3a5                                      0.1s
 => => extracting sha256:c80762877ac59b755105fb2ab333f35c02bb8ad616267989de82a6d475daa051                                      0.3s
 => => extracting sha256:86f9cc2995adc9ec276a7963ba4592bfddcff8901088fea7907999f5ffce55dc                                      0.0s
 => [2/2] WORKDIR /app                                                                                                         1.3s
 => exporting to image                                                                                                         0.1s
 => => exporting layers                                                                                                        0.0s
 => => exporting manifest sha256:107fa18ccdc4ed8086e67289e7690246b7e122416dbe9852a9a0dd83f9948a44                              0.0s
 => => exporting config sha256:86c1bf8b2b00ec331c3bba2a4ec5b1456c0b5b5782a44af1f0eb9d98e193442c                                0.0s
 => => exporting attestation manifest sha256:dd3140efc76f93c03036258923b2af698af6b7a18986fd1a634db8092d598f4c                  0.0s
 => => exporting manifest list sha256:0fb503a9ad1a0901a847ebbafb3713e20041dfb03fce146f03f9e0eb35500c89                         0.0s
 => => naming to docker.io/library/python-assignment:latest                                                                    0.0s
 => => unpacking to docker.io/library/python-assignment:latest                                                                 0.0s

View build details: docker-desktop://dashboard/build/desktop-linux/desktop-linux/4j2n97u4b4hanb0lhe1u8bm7g

What's next:
    View a summary of image vulnerabilities and recommendations → docker scout quickview 
adamduda@Adams-MacBook-Pro Assignment01 % docker run -it python-assignment
root@b0931a52a93e:/app# pip --version
pip 24.3.1 from /usr/local/lib/python3.12/site-packages/pip (python 3.12)
root@b0931a52a93e:/app# exit
exit
adamduda@Adams-MacBook-Pro Assignment01 % 
```

In particular:

```
root@b0931a52a93e:/app# pip --version
pip 24.3.1 from /usr/local/lib/python3.12/site-packages/pip (python 3.12)
```
