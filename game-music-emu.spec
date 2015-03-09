Summary:	Collection of video game music file emulators
Summary(pl.UTF-8):	Zbiór emulatorów do odtwarzania muzyki z gier
Name:		game-music-emu
Version:	0.6.0
Release:	2
License:	LGPL v2.1+
Group:		Libraries
#Source0Download: http://code.google.com/p/game-music-emu/downloads/list
Source0:	http://game-music-emu.googlecode.com/files/%{name}-%{version}.tar.bz2
# Source0-md5:	b98fafb737bc889dc65e7a8b94bd1bf5
Patch0:		%{name}-multilib.patch
URL:		http://code.google.com/p/game-music-emu/
BuildRequires:	cmake >= 2.6
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Game_Music_Emu is a collection of video game music file emulators that
support the following formats and systems:

- AY - ZX Spectrum/Amstrad CPC
- GBS - Nintendo Game Boy
- GYM - Sega Genesis/Mega Drive
- HES - NEC TurboGrafx-16/PC Engine
- KSS - MSX Home Computer/other Z80 systems (doesn't support FM sound)
- NSF/NSFE - Nintendo NES/Famicom (with VRC 6, Namco 106, and FME-7
  sound)
- SAP - Atari systems using POKEY sound chip
- SPC - Super Nintendo/Super Famicom
- VGM/VGZ - Sega Master System/Mark III, Sega Genesis/Mega Drive, BBC
  Micro

%description -l pl.UTF-8
Game_Music_Emu to zbiór emulatorów pozwalających na odtwarzanie plików
muzycznych z gier. Obsługiwane formaty i systemy to:

- AY - ZX Spectrum/Amstrad CPC
- GBS - Nintendo Game Boy
- GYM - Sega Genesis/Mega Drive
- HES - NEC TurboGrafx-16/PC Engine
- KSS - MSX Home Computer/inne systemy Z80 (bez obsługi dźwięku FM)
- NSF/NSFE - Nintendo NES/Famicom (z dźwiękiem VRC 6, Namco 106 i
  FME-7)
- SAP - systemy Atari wykorzystujące układ dźwiękowy POKEY
- SPC - Super Nintendo/Super Famicom
- VGM/VGZ - Sega Master System/Mark III, Sega Genesis/Mega Drive, BBC
  Micro

%package devel
Summary:	Header files for game-music-emu library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki game-music-emu
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
This package contains the header files for developing applications
that use game-music-emu library.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe do tworzenia aplikacji
wykorzystujących bibliotekę game-music-emu.

%prep
%setup -q
%patch0 -p1

%build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DLIB_INSTALL_DIR=%{_libdir} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
	-DCMAKE_CXX_FLAGS_RELEASE="-DNDEBUG" \
	-DCMAKE_VERBOSE_MAKEFILE=ON

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc changes.txt design.txt gme.txt readme.txt
%attr(755,root,root) %{_libdir}/libgme.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgme.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgme.so
%{_includedir}/gme
%{_pkgconfigdir}/libgme.pc
