Name:           pypoker-eval
Version:        133.0
Release:        %mkrel 4
Epoch:          0
Summary:        Python interface to poker-eval
Group:          Development/Python
License:        GPL
URL:            http://pokersource.org/pypoker-eval/
Source0:        http://download.gna.org/pokersource/sources/%{name}-%{version}.tar.bz2
BuildRequires:  poker-eval-devel >= 0:133.0
BuildRequires:  python-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
This package is python adaptor for the poker-eval toolkit for
writing programs which simulate or analyze poker games.

%package -n python-pokereval
Summary:        Python interface to poker-eval
Group:          Development/Python
Provides:       %{name} = %{epoch}:%{version}-%{release}

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

# make examples directory for devel %doc
%{__mkdir} -p tmp/examples && %{__cp} -a test.py tmp/examples

%build
%{configure2_5x} --disable-static
%{make}

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}

%check
%{__python} test.py
 
%clean
%{__rm} -rf %{buildroot}

%files -n python-pokereval
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README
%{python_sitearch}/*.so.*
%{python_sitearch}/*.py
%{python_sitearch}/*.pyc
%{python_sitearch}/*.pyo
%{python_sitearch}/*.so
%{python_sitearch}/*.la

%files -n python-pokereval-devel
%defattr(-,root,root,-)
%doc tmp/examples
%{_libdir}/pkgconfig/%{name}.pc

