find . -name *morph | xargs sed -i -e "s/^- morph: strata\//- name: /"
find . -name *morph | xargs sed -i -e "s/^- morph: systems\//- name: /"
find . -name *morph | xargs sed -i -e "s/\.morph//"
find . -name *morph | xargs sed -i -e "s/strata:/contents:/"
find . -name *morph | xargs sed -i -e "s/chunks:/contents:/"
find . -name *morph | xargs sed -i -e "/morph: /d"
find . -name *morph | xargs sed -i -e "/build-depends: \[\]/d"