Name:		linux-firmware
Version:	20100106
Release:	1%{?dist}
Summary:	Firmware files used by the Linux kernel

Group:		System Environment/Kernel
License:	GPL+ and GPLv2+ and MIT and Redistributable, no modification permitted
URL:		http://www.kernel.org/
Source0:	ftp://ftp.kernel.org/pub/linux/kernel/people/dwmw2/firmware/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch
Provides:	kernel-firmware = %{version}
Obsoletes:	kernel-firmware < %{version}
Requires:	udev

%description
Kernel-firmware includes firmware files required for some devices to
operate.

%prep
%setup -q -n linux-firmware-%{version}


%build
# Remove firmware shipped in separate packages already
# Perhaps these should be built as subpackages of linux-firmware?
rm ql2???_fw.bin LICENCE.qla2xxx
rm iwlwifi-*.ucode LICENCE.iwlwifi_firmware
rm -rf ess korg sb16 yamaha
# We have _some_ ralink firmware in separate packages already.
rm rt73.bin rt2561.bin rt2561s.bin rt2661.bin
# And _some_ conexant firmware.
rm v4l-cx23418-apu.fw v4l-cx23418-cpu.fw v4l-cx23418-dig.fw v4l-cx25840.fw

# Remove source files we don't need to install
rm -f usbdux/*dux */*.asm

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/lib/firmware
cp -r * $RPM_BUILD_ROOT/lib/firmware
rm $RPM_BUILD_ROOT/lib/firmware/{WHENCE,LICENCE.*}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc WHENCE LICENCE.*
/lib/firmware/*

%changelog
* Wed Jan 06 2010 David Woodhouse <David.Woodhouse@intel.com> 20090106-1
- Update

* Fri Aug 21 2009 David Woodhouse <David.Woodhouse@intel.com> 20090821-1
- Update, fix typos, remove some files which conflict with other packages.

* Thu Mar 19 2009 David Woodhouse <David.Woodhouse@intel.com> 20090319-1
- First standalone kernel-firmware package.
