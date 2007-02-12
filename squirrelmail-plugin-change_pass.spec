%define		_plugin	change_pass
%define		_plugin_version 2.7
%define		_squirrel_version_required 1.4.x
%define		_version_rpm %{_plugin_version}_%{_squirrel_version_required}
%define		_version_tgz %{_plugin_version}-%{_squirrel_version_required}
Summary:	A squirrel interface to change passwords
Summary(pl.UTF-8):   Wiewiórczy interfejs do zmiany haseł
Name:		squirrelmail-plugin-%{_plugin}
Version:	%{_plugin_version}_%{_squirrel_version_required}
Release:	1
License:	GPL
Group:		Applications/Mail
Source0:	http://www.squirrelmail.org/plugins/%{_plugin}-%{_version_tgz}.tar.gz
# Source0-md5:	590e0b3e879bffdb4dea57d369618353
URL:		http://www.squirrelmail.org/plugin_view.php?id=21
Requires:	squirrelmail >= 1.4.6-2
Requires:	poppassd
Obsoletes:	squirrelmail-change_pass
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_squirreldir	%{_datadir}/squirrelmail
%define		_squirreldata	/var/lib/squirrelmail
%define		_plugindir	%{_squirreldir}/plugins/%{_plugin}

%description
This package contains a interface to change passwords using poppassd
protocol.

%description -l pl.UTF-8
Ten pakiet zawiera interfejs do zmiany haseł poprzez protokół
poppassd.

%prep
%setup -q -n %{_plugin}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_plugindir}

cp -R *.php locale $RPM_BUILD_ROOT%{_plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%{_plugindir}
