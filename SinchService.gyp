{
    'configurations': { # project-wide configurations
        'Debug': {
            'xcode_settings': {
                'SDKROOT': 'iphoneos',
                'ONLY_ACTIVE_ARCH': 'YES',
            },
        },
        'Release': {
            'xcode_settings': {
                'SDKROOT': 'iphoneos'
            },
        },
    }, 
    'target_defaults': {
        'configurations': {
            'Release': {
                'defines': [
                    'NDEBUG',
                    'NS_BLOCK_ASSERTIONS=1', # Block Cocoa-asserts (NSAssert(...))
                ],
            },
            'Debug': {
                'defines': [
                    '_DEBUG',
                    'DEBUG=1',
                ],
                'xcode_settings': {
                    'ONLY_ACTIVE_ARCH': 'YES',
                    'DEBUG_INFORMATION_FORMAT': 'dwarf', # faster than dwarf+dSYM
                    'GCC_OPTIMIZATION_LEVEL': '0', # stop gyp from defaulting to -Os
                },
            },
        },
        'xcode_settings': {
            'INFOPLIST_FILE': '${PRODUCT_NAME}/Info.plist',
            'CLANG_ENABLE_OBJC_ARC': 'YES',
            'GCC_WARN_PEDANTIC': 'YES',
            'GCC_TREAT_WARNINGS_AS_ERRORS': 'YES',
            'IPHONEOS_DEPLOYMENT_TARGET': '6.0',
            'HEADER_SEARCH_PATHS': ['.', 'SinchService/PrivateHeaders'],
        },
        'default_configuration': 'Release',
    },
    'targets': [
        {
            'target_name': 'SinchService',
            'type': 'static_library',
            'mac_bundle': 0,
            'sources' : [ 
                '<!@(ls -1 SinchService/*.h)' ,
                '<!@(ls -1 SinchService/*.m)' 
            ],
        },     
    ],
}
