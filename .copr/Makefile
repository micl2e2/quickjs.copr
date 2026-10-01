
packages:
	dnf --quiet -y install git tree gcc

create_source_rpm:
	curl --location https://codeload.github.com/micl2e2/quickjs/tar.gz/7754c8eb4a8db331c14df46ee54f3be68a2a83fb --output quickjs.tar.gz
	mv quickjs.tar.gz /builddir/build/SOURCES
	rpmbuild -bs $(spec)

all_source_rpm_to_workdir:
	tree ~/build
	mv ~/build/SRPMS/*.src.rpm $(outdir)

srpm: packages create_source_rpm all_source_rpm_to_workdir
	echo SRPM done

