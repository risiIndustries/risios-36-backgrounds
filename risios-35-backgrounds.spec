Name:		risios-35-backgrounds
Version:	0.1
Release:	2%{?dist}
Summary:	Wallpapers for risioS

License:	GPL v3
URL:		risi.io
Source0:	https://github.com/risiOS/risios-35-backgrounds/archive/refs/heads/main.tar.gz#/risios-35-backgrounds-main.tar.gz

BuildArch:	noarch

%description
Wallpapers for risiOS

%prep
%autosetup -n risios-35-backgrounds-main
%build

%install
mkdir -p %{buildroot}%{_datadir}/backgrounds/risios-35-backgrounds/
cp -R *.png %{buildroot}%{_datadir}/backgrounds/risios-35-backgrounds/
cp -R *.jpg %{buildroot}%{_datadir}/backgrounds/risios-35-backgrounds/
mkdir -p %{buildroot}%{_datadir}/gnome-background-properties
cp risios-35-backgrounds.xml %{buildroot}%{_datadir}/gnome-background-properties/risios-35-backgrounds.xml

%files
%{_datadir}/backgrounds/risios-35-backgrounds/*
%{_datadir}/gnome-background-properties/risios-35-backgrounds.xml

%changelog
* Sun Jan 9 2022 PizzaLovingNerd
- risiOS 35 Wallpapers
