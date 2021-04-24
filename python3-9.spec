Name:           python3
Version:        %{_python3version}
Release:        1%{?dist}
Summary:        Example Python3.9 RPM
License:        MIT
# URL:            
# Source0:        

%description
Installs python3.9 in /opt/python3-9 directory built from https://github.com/python/cpython branch 3.9

%prep


%build


%install
cp -a 

%files
%defattr(755, root, root, 755)
/opt/*
