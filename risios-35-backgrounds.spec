Name:           risios-35-backgrounds
Version:        0.1
Release:        1%{?dist}
Summary:        Wallpapers for risioS

License:        GPL v3
URL:            risi.io
Source0:        https://github.com/risiOS/risios-35-backgrounds/archive/refs/heads/main.tar.gz#/risios-35-backgrounds-main.tar.gz

BuildArch:	noarch

%description
Wallpapers for risiOS

%prep
%autosetup -n risios-35-backgrounds-main
%build

%install
%dir %{_datadir}/backgrounds/risios-35/
cp -R * %{_datadir}/backgrounds/risios-35/

%files
%{_datadir}/backgrounds/risios-35/*
	
%changelog
* Sun Jan 9 2022 PizzaLovingNerd
- risiOS 35 Wallpapers
