Summary:	Clone of the C64 Game Paradroid
Summary(pl):	Klon gry Paranoid z C64
Name:		freedroid
Version:	1.0.1
Release:	2
License:	GPL
Group:		Applications/Games
Source0:	http://dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	a4350ce4695d1ab65db7b6e1d7124863
Source2:	%{name}.desktop
URL:		http://freedroid.sourceforge.net/
BuildRequires:	SDL-devel >= 1.2.3
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_image-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a clone of the classic game "Paradroid" on Commodore 64 with
some improvements and extensions to the classic version.

%description -l pl
Jest to klon klasycznej gry "Paranoid" na Commodore 64 z kilkoma
ulepszeniami i dodatkami.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_applnkdir}/Games

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE2} $RPM_BUILD_ROOT/%{_applnkdir}/Games

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_applnkdir}/Games/*
%{_mandir}/man6/*
