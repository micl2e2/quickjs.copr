%global upstream_date 2026-06-04
# qjsq and extra.Makefile are not in the commit used by the other specs.
%global commit 7754c8eb4a8db331c14df46ee54f3be68a2a83fb
# Fedora runs %%set_build_flags at the start of %%build, %%check, and
# %%install. Leave the compiler flags to the QuickJS Makefile.
%undefine _auto_set_build_flags
# Do not add debuginfo packages or /usr/lib/.build-id links.
%global debug_package %{nil}
%global _build_id_links none

Name:           quickjs.extra
Version:        2026.06.04
Release:        1%{?dist}
Summary:        WIP

License:        MIT
URL:            https://github.com/micl2e2/quickjs
# Source0:        https://codeload.github.com/micl2e2/quickjs/tar.gz/%{commit}
Source0:        quickjs.tar.gz

BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  make

%description
WIP

%prep
# The codeload archive unpacks to quickjs-<full commit>, not %{name}.
%setup -q -n quickjs-%{commit}

%build
# extra.Makefile builds qjsc, compiles qjsq.js to C, and links qjsq.
# qjsc is only a build tool. This package installs qjsq.
%make_build -f extra.Makefile PREFIX=%{_prefix} qjsq

%install
install -D -p -m 0755 qjsq %{buildroot}%{_bindir}/qjsq

%check
test "$(printf '%s' '{"hello":"world"}' | ./qjsq .hello)" = "world"
test "$(printf '%s' '[10,20]' | ./qjsq '[1]')" = "20"

%files
%{_bindir}/qjsq

%changelog
* Wed Sep 30 2026 Packager - 2026.06.04-1
- WIP
