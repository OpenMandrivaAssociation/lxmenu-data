Summary:	Menu data files for LXDE
Name:		lxmenu-data
Version:	0.1.5
Release:	3
Source0:	http://dfn.dl.sourceforge.net/sourceforge/lxde/%{name}-%{version}.tar.gz
License:	GPLv2+
Group:		Graphical desktop/Other
Url:		http://lxde.sourceforge.net/
BuildRequires:	intltool
BuildRequires:	glib-gettextize
BuildRequires:	gettext-devel
BuildArch:	noarch

%description
This package provides files required to build freedesktop.org menu
spec-compliant desktop menus for LXDE.

The files are originally taken from gnome-menus, and some minor
modifications were made.

%prep
%setup -q
[ -e autogen.sh ] && ./autogen.sh

%build
%configure
%make_build

%install
%make_install

%files
%{_datadir}/desktop-directories/lxde-*.directory
%{_sysconfdir}/xdg/menus/lxde-applications.menu
