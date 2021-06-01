from distutils.core import setup, Extension

netconf2Module = Extension("netconf2",
                           sources=["src/netconf.c",
                                    "src/session.c",
                                    "src/ssh.c",
                                    "src/tls.c",
                                    "src/rpc.c",
                                    "src/err.c"
                                   ],
                           depends=["src/netconf.h",
                                    "src/session.h",
                                    "src/rpc.h"
                                   ],
                           # libraries=["netconf2"],
                           extra_compile_args=["-Wall", "-I./src", "-DNC_ENABLED_SSH", "-DNC_ENABLED_TLS"],
                           # extra_link_args=[""],
                        )

setup(name='netconf2',
      version='1.1.43',
      author='Radek Krejci',
      author_email='rkrejci@cesnet.cz',
      description='libnetconf2 Python bindings.',
      long_description = 'TBD',
      url='https://github.com/CESNET/libnetconf2',
      ext_modules=[netconf2Module],
      platforms=['Linux'],
      license='BSD License',
      )
