Summary:	Clone of the C64 Game Paradroid
Summary(pl):	Klon gry Paranoid z C64
Name:		freedroid
Version:	1.0.2
Release:	3
License:	GPL
Group:		Applications/Games
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	585a65f61c2cd308ab45d5c514f695dc
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://freedroid.sourceforge.net/
BuildRequires:	SDL-devel >= 1.2.3
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	automake
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
cp /usr/share/automake/config.sub .
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*
%{_pixmapsdir}/*
%{_mandir}/man6/*
