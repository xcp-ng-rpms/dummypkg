Summary:        Dummy package for test purpose
Name:           dummypkg
Version:        1.0
Release:        2%{?dist}
License:        Public Domain
URL:            https://github.com/xcp-ng-rpms/dummypkg

BuildArch:      noarch

%description
%{summary}

%package extra
Summary:        Extra dummy package

%description extra
Extra dummy package

%prep
# A change

%build

%install

%files

%files extra

%changelog
* Fri Oct 14 2022 Samuel Verschelde <stormi-xcp@ylix.fr> - 1.0-2
- Build an updated package for updater tests

* Thu Oct 13 2022 Benjamin Reis <benjamin.reis@vates.fr> - 1.0-1
- Create dummypkg RPM
