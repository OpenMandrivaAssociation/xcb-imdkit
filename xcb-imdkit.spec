%define major 1
%define libname %mklibname xcb-imdkit
%define devname %mklibname xcb-imdkit -d

Name:		xcb-imdkit
Version:	0.0
Release:	0.20250130.1
Source0:	https://github.com/fcitx/xcb-imdkit/archive/refs/heads/master.tar.gz#/%{name}-%{release}.tar.gz
Summary:	Input method development support for XCB
URL:		https://github.com/fcitx/xcb-imdkit
License:	LGPL-2+
Group:		System/Libraries
BuildRequires:	cmake
BuildSystem:	cmake
BuildRequires:	pkgconfig(xcb)
BuildRequires:	pkgconfig(xcb-util)
BuildRequires:	pkgconfig(xcb-keysyms)

%description
xcb-imdkit is an implementation of xim protocol in xcb, comparing with the
implementation of IMDkit with Xlib, and xim inside Xlib, it has less memory
foot print, better performance, and safer on malformed client.

And not to say it's all asynchronous and it works with xcb.

Though, it doesn't have complete protocol support, since some part of the
protocol is never used. Those parts include:

* XIM_EXT_SET_EVENT_MASK (no im actually use this)
* XIM_EXT_FORWARD_EVENT (it's not any better than forward event)
* XIM_AUTH (IMDkit doesn't implement this, Xlib only has stub, so still no implementation.)
* XIM_STR_CONVERSION (Synchronous protocol, but not used anywhere)
* Locale check on client side, this is actually very evil for input method.
* Only X transport is supported.

%package -n %{libname}
Summary:	Input method development support for XCB
Group:		System/Libraries

%description -n %{libname}

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Input method development support for XCB

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_libdir}/cmake/*
