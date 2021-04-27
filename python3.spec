# Turn off the brp-python-bytecompile automagic
%global _python_bytecompile_extra 0
%undefine __python
%undefine __python3
# Don't delete build folder
%define __spec_install_pre /bin/true

Name:           python3
Version:        %{_python3version}
Release:        1%{?dist}
Summary:        Example Python3 RPM built from %{_python3branch}
License:        Python
  

%description
Installs python3 in %{_installdir} directory built from https://github.com/python/cpython branch %{_python3branch}

%prep
# Nothing 

%build
# Nothing

%install
# Create the install folder
mkdir -p %{buildroot}%{_installdir}

# Fix annoying path in cgi.py
sed -i 's|^#! /usr.*|#!'"%{_installdir}/bin/python3"'|g' %{buildroot}/../BUILD/lib/python3*/cgi.py

cp -ar %{buildroot}/../BUILD/* %{buildroot}/%{_installdir}


%files
%defattr(-, root, root, -)
/opt/*
