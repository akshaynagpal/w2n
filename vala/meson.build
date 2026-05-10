project('W2N project', 
        ['vala', 'c'],
        version: 'w2ni18n-0.1.0',
        license: 'MIT')

target_vala = '0.52'


glib = dependency('glib-2.0', version: '>=2.62')
gobject = dependency('gobject-2.0')
gee = dependency('gee-0.8')


dependencies = [
    glib,
    gobject,
    gee,
]

sources = files()

subdir('src')

executable('W2N', sources, dependencies: dependencies)
library ('W2N', sources, dependencies: dependencies)
