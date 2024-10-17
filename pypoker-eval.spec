Name:           pypoker-eval
Version:        138.0
Release:        %mkrel 1
Epoch:          0
Summary:        Python interface to poker-eval
Group:          Development/Python
License:        GPLv3+
URL:            https://pokersource.org/pypoker-eval/
Source0:        http://download.gna.org/pokersource/sources/pypoker-eval-%{version}.tar.gz
Patch0:		pypoker-eval-137.0-py2.7.patch
BuildRequires:  poker-eval-devel
BuildRequires:  python-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
This package is python adaptor for the poker-eval toolkit for
writing programs which simulate or analyze poker games.

%package -n python-pokereval
Summary:        Python interface to poker-eval
Group:          Development/Python
Provides:       %{name} = %{epoch}:%{version}-%{release}
%py_requires -d

%description -n python-pokereval
This package is python adaptor for the poker-eval toolkit for
writing programs which simulate or analyze poker games.

%package -n python-pokereval-devel
Summary:        Files needed for developing programs which use pypoker-eval
Group:          Development/Python
Provides:       %{name}-devel = %{epoch}:%{version}-%{release}
Requires:       python-pokereval = %{epoch}:%{version}-%{release}
Requires:       pkgconfig

%description -n python-pokereval-devel
This package contains files required to build applications that use
pypoker-eval.

%prep
%setup -q
%patch0 -p0

# make examples directory for devel %doc
%{__mkdir} -p tmp/examples
%{__cp} -a test.py tmp/examples

%build
autoreconf -fi
%{configure2_5x} --disable-static
%{make}

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}

%clean
%{__rm} -rf %{buildroot}

%check
%{__python} test.py

%files -n python-pokereval
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README
%{python_sitearch}/*

%files -n python-pokereval-devel
%defattr(-,root,root,-)
%doc tmp/examples
%{_libdir}/pkgconfig/%{name}.pc
