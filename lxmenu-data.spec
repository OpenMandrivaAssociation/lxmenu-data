# git snapshot
%global snapshot 1
%if 0%{?snapshot}
	%global commit		6ffc8b388792fc89d40850bb2b6d28e16eb7f1a3
	%global commitdate	20230801
	%global shortcommit	%(c=%{commit}; echo ${c:0:7})
%endif

Summary:	Menu data files for LXDE
Name:		lxmenu-data
Version:	0.1.6
Release:	1
#Source0:	http://dfn.dl.sourceforge.net/sourceforge/lxde/%{name}-%{version}.tar.gz
Source0:	https://github.com/lxde/%{name}/archive/%{?snapshot:%{commit}}%{!?snapshot:%{version}}/%{name}-%{?snapshot:%{commit}}%{!?snapshot:%{version}}.tar.gz
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

%files
%{_datadir}/desktop-directories/lxde-*.directory
%{_sysconfdir}/xdg/menus/lxde-applications.menu

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-%{?snapshot:%{commit}}%{!?snapshot:%{version}}

%build
autoreconf -fiv
%configure \
	--enable-gtk3 \
	%{nil}
%make_build

%install
%make_install

