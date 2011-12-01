%define	version	2.4.2
%define release %mkrel 8
%define dict_format_version	2.4.2

Summary:	Turkish -> German Freedict dictionary for StarDict 2
Name:		stardict-freedict-tur-deu
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Databases
URL:		http://stardict.sourceforge.net/
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildArch:	noarch

Source0:	ftp://osdn.dl.sourceforge.net/pub/sourceforge/s/st/stardict/stardict-dictd_www.freedict.de_tur-deu-%{version}.tar.bz2

Provides:	stardict-dictionary = %{dict_format_version}
Requires:	stardict >= %{dict_format_version}

%description
Turkish -> German Freedict dictionary in StarDict 2 format

%prep
%setup -q -n stardict-dictd_www.freedict.de_tur-deu-%{version}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/stardict/dic
install -m 0644 * %{buildroot}%{_datadir}/stardict/dic

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/stardict/dic/*


