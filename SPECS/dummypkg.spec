Summary:        Dummy package for test purpose
Name:           dummypkg
Version:        1.0
Release:        1%{?dist}
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

%build

%install

%files

%files extra

%changelog
* Thu Oct 13 2022 Benjamin Reis <benjamin.reis@vates.fr> - 1.0-1
- Create dummypkg RPM
