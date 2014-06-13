Summary:	Menu data files for LXDE
Name:		lxmenu-data
Version:	0.1.2
Release:	6
License:	GPLv2+
Group:		Graphical desktop/Other
Url:		http://lxde.sourceforge.net/
Source0:	http://dfn.dl.sourceforge.net/sourceforge/lxde/%{name}-%{version}.tar.gz
BuildRequires:	intltool
BuildArch:	noarch

%description
This package provides files required to build freedesktop.org menu
spec-compliant desktop menus for LXDE.

The files are originally taken from gnome-menus, and some minor
modifications were made.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%{_datadir}/desktop-directories/lxde-*.directory
%{_sysconfdir}/xdg/menus/lxde-applications.menu

