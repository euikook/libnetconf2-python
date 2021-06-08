from setuptools import setup, Extension

netconf2_module = Extension("netconf2",
                           sources=["netconf.c",
                                    "session.c",
                                    "ssh.c",
                                    "tls.c",
                                    "rpc.c",
                                    "err.c"
                                    ],

                           depends=["netconf.h",
                                    "session.h",
                                    "rpc.h"],
                           libraries=["netconf2"],
                           extra_compile_args=["-Wall", "-I.", "-DNC_ENABLED_SSH", "-DNC_ENABLED_TLS"],
                           extra_link_args=[],
                        )

setup(name='netconf2',
      version='0.1.0',
      # author='euikook',
      # author_email='euikook@gmail.com',
      # description='libnetconf2 Python bindings. forked from CSNET',
      # long_description = 'TBD',
      # url='https://github.com/euikook/libnetconf2-python',
      ext_modules=[netconf2_module],
      # platforms=['Linux'],
      # license='BSD License',
      )
