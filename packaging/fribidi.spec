
Name:       fribidi
Summary:    Library implementing the Unicode Bidirectional Algorithm
Version:    0.19.2
Release:    1
Group:      System/Libraries
License:    LGPLv2+
URL:        http://fribidi.org
Source0:    http://fribidi.org/download/%{name}-%{version}.tar.gz
Patch0:     donotuse_page_size.patch
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  pkgconfig


%description
A library to handle bidirectional scripts (for example Hebrew, Arabic),
so that the display is done in the proper way; while the text data itself
is always written in logical order.



%package devel
Summary:    Libraries and include files for FriBidi
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Include files and libraries needed for developing applications which use
FriBidi.



%prep
%setup -q -n %{name}-%{version}

# donotuse_page_size.patch
%patch0 -p1

%build

%configure --disable-static
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install




%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig





%files
%defattr(-,root,root,-)
%doc README AUTHORS COPYING ChangeLog THANKS NEWS TODO
%{_bindir}/fribidi
%{_libdir}/libfribidi.so.*


%files devel
%defattr(-,root,root,-)
%{_includedir}/fribidi
%{_libdir}/libfribidi.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/%{name}_*.gz

