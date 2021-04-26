# Turn off the brp-python-bytecompile automagic
%global _python_bytecompile_extra 0
%undefine __python
%undefine __python3
# Don't delete build folder
%define __spec_install_pre /bin/true

Name:           python3
Version:        %{_python3version}
Release:        1%{?dist}
Summary:        Example Python3.9 RPM
License:        Python
# URL:            
# Source0:        

%description
Installs python3.9 in %{_installdir} directory built from https://github.com/python/cpython branch 3.9

%prep


%build


%install
# Create the install folder
mkdir -p %{buildroot}%{_installdir}

# Remove references to the prefix used for the build
sed -i 's|^#!/tmp.*|#!'"%{_installdir}/bin/python3"'|g' %{buildroot}/../BUILD/bin/*
sed -i 's|^#!/tmp.*|#!'"%{_installdir}/bin/python3"'|g' %{buildroot}/../BUILD/lib/python3*/config*/python-config.py
sed -i 's|^#! /usr.*|#!'"%{_installdir}/bin/python3"'|g' %{buildroot}/../BUILD/lib/python3*/cgi.py

# Make sure no references exist


cp -ar %{buildroot}/../BUILD/* %{buildroot}/%{_installdir}


%files
%defattr(-, root, root, -)
/opt/*
