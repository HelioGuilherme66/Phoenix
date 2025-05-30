.. title: wxPython Changelog
.. slug: changes
.. author: Robin
.. description: Summary of changes for wxPython releases
.. type: text


wxPython Changelog
==================




4.2.4
------
* (unreleased)

PyPI:   https://pypi.python.org/pypi/wxPython/4.2.4
Extras: https://extras.wxPython.org/wxPython4/extras/
Pip:    ``pip install wxPython==4.2.4``

New and improved in this release:




4.2.3
------
* 9-Apr-2025

PyPI:   https://pypi.python.org/pypi/wxPython/4.2.3
Extras: https://extras.wxPython.org/wxPython4/extras/
Pip:    ``pip install wxPython==4.2.3``

New and improved in this release:
* This release was built using the wxWidgets' v3.2.7 release tag.  The only exception is that libtiff and pcre2 bundled with wxWidgets are updated to the versions from the wxWidgets master branch (libtiff 4.7.0 and pcre2 10.44).

* Fix test issues with wx.lib.introspect (#2717)

* Add support for building on Windows ARM64 (#2521)

* Incorporate many improvements to type stubs (#2665)

* Fix building documentation with latest sphinx (#2672)

* Build smaller architecture-specific wheels on macOS instead of large universal2 wheels

* Calculate scroll based on child's relative position to scrolledpanel in wx.lib.scrolledpanel

* Fix float -> int conversion issues in wx.lib.fancytext (#2703)

* Replace deprecated NumPy type aliases

* Use wx.StaticText in wx.lib.agw.hyperlink (#2686)

* Implement partial support for pyproject.toml and other build process improvements

* Remove use of six and most Python 2 compatibility code

* Fix wxWidgets build on OpenSUSE (#558, #1067, #2422, #2532)

* Fix more int conversions in wx.lib.agw.flatnotebook

* Make build output reproducible

* Enable overridding wx.Sizer.InformFirstDirection() (#2452)

* Implement __iter__ for wxList iterator classes (fixes Python 3.13.1 issue)

* Fix wx.lib.mixins.rubberband not clearing DC on redraw

* Support implementing CreateBitmapBundle for custom ArtProvider

* Fix float/int conversion issues in wx.lib.ogl

* Include usage of `wxMemoryFSHandler` in webview demo

* Fix crash when accessing wx.stc.StyledTextCtrl.DropTarget.Data (#2043)

* Fix AuiManager pane minimizing issue

* Add range field to wx.lib.agw.pygauge.PyGauge format string (#2583)

* Fix pickling of wx.RealPoint (#2644)

* Avoid calling FlatMenu Destroy() in a finally block (#2630)

* Update wxApp.IsDisplayAvailable to work on Wayland

* Fix InspectionTool crashes due to bad perspective string errors

* Drop support for Python 3.8 (EOL)

* Add CreateAccessible for Windows only

* Added check condition to AuiManager LoadPerspective()

* Fix RecursionError in platebtn bitmap getters

* Add Python implementation of GetPaths (#1944)

* Support Wayland GTK backend in Window.GetHandle

* Refactor python only pdfviewer to support displaying pdf files where not all pages have the same size

* Improve support when specifying a pre-existing toolbar as the target for the restore icon when minimizing a pane in agw.aui

* Multiple bugfixes in pure python aui

* pdfviewer: Add support for pymupdf renaming




4.2.2
------
* 11-Sept-2024

PyPI:   https://pypi.python.org/pypi/wxPython/4.2.2
Extras: https://extras.wxPython.org/wxPython4/extras/
Pip:    ``pip install wxPython==4.2.2``

New and improved in this release:
* This release was built using the wxWidgets' v3.2.6 release tag.  This is the first release built using GitHub infrastructure instead of the buildbots.  Please report any problems with the wheels.

* Fix some Python 3.12 compatibility issues (segfault on exit) by upgrading sip & waf

* Fix more float/int conversion issues in wx.lib classes (#2415, #2417, #2429, #2470, #2528, #2542)

* Add initialValue argument to wx.lib.DirBrowseButton (#2430)

* Fix wxImage.Clear() (#2433)

* Fix blurry text in AuiNotebook tab (#2360)

* Add support for frozen rows and columns to GridWithLabelRenderersMixin (#2436)

* demo: ShortcutEditor: Fix broken call GetMenuBar() (#2412)

* Add proper support for DataViewCheckIconTextRenderer (#2425)

* Remove legacy macOS logic, use wx.SystemSettings to select colors (#2018)

* Build: Use new tarfile.extractall() filter for safer tarfile extraction (#2443)

* Fix typo in wx.lib.agw.persist_handlers (#2469)

* Fix 'str' to 'wxString' converstation, when emoji is inside string (#2446)

* Use unwrap before isbuiltin check (#2487)

* Preserve pane icons when loading a perspective in agw.aui (#2494)

* wx.agw.aui: don't uninitialize the AuiManager if the window close event is vetoed (#2460)

* Pure python AUI: Make behavior in all platforms more equal (#2501)

* wx.agw.aui. Do layout as the last step after all pane infos have recomputed their best sizes (#2500)

* Fix additional SyntaxWarnings with Python 3.12 (#2502)

* Fix wx.lib.agw.ribbon.RibbonButtonBar DeleteButton function (#2511)

* UltimateListCtrl: Add support for ULC_AUTO_CHECK_PARENT (#2518)

* Remove dependency on distutils (#2519)

* Improve wx.lib.agw.FlatMenu memory usage (#2373)

* Support NumPy 2.0 (#2580, 2591)

* Fix EditLabel on CustomTreeCtrl doesn't automatically select the entire text (#2549)

* Fix Widgets placed in the UltimateListControl are drawn in the wrong location (#2410)

* Fix wx.lib.agw.aui sometimes shows "ghost" docking guide (#2364)

* Fix Thumbnailctrl SetSelection raises exception if it tries to scroll (#2345)




4.2.1 "Size matters not." (Yoda)
--------------------------------
* 7-June-2023

PyPI:   https://pypi.python.org/pypi/wxPython/4.2.1
Extras: https://extras.wxPython.org/wxPython4/extras/
Pip:    ``pip install wxPython==4.2.1``

New and improved in this release:

* This release was built using the wxWidgets' v3.2.2.1 release tag.

* Added Python 3.11 to the build system.

* Added Python 3.12 (beta) to the build system.

* Added wrappers for wxGenericStaticBitmap.

* Added wx.ThreadEvent.




4.2.0 "Rumors of my death are only slightly exaggerated"
--------------------------------------------------------
* 7-Aug-2022

PyPI:   https://pypi.python.org/pypi/wxPython/4.2.0
Extras: https://extras.wxPython.org/wxPython4/extras/
Pip:    ``pip install wxPython==4.2.0``

New and improved in this release:

* Yes, it's been a VERY long time since the last release. I'm not dead, just on
  an extended break. It took me a while to get up to speed on a new day job, and
  then there was a seemingly perpetual crunch-mode to get the product through a
  couple release cycles. I can't say that things are fully back to normal yet,
  but at least I now know what I'm doing. Mostly. <wink>

* This release is built using the wxWidgets' 3.2.0 release tag.

* Tweaked the build scripts a bit to ensure that on non-Windows platforms that
  the compiler and flags used by default match those used by wxWidgets, (with
  the flags needed by Python added on.) The compiler commands can be overridden
  by setting CC and CXX in the environment if needed. (#1247)

* On Windows the build code that locates and sets up the environment for the
  MSVC compiler no longer relies on distutils code, but is now using more modern
  code in setuptools instead. This enables much more compiler flexibility and
  wxPython should now be buildable with Visual Studio versions from 2015 through
  2022+.

* Switched to SIP 6 for generating the wrapper code. Rather than a standalone
  executable, SIP is now a Python package that needs to be installed in the
  Python environment used for the build. A dependency has been added to
  requirements/devel.txt to help ensure that the correct version is installed.
  The wx.siplib module code is no longer kept in the repository, but is
  generated during the build.

* Changed wx.App.InitLocale to just do `locale.setlocale(locale.LC_ALL, "C")`
  to undo what Python (3.8+ on Windows) does. This lets wxWidgets start with an
  uninitialized locale as it expects. (#1637)

* Fixed issues related to `time_t` always being treated as a 32-bit value on
  Windows. (#1910)

* Added wx.FullScreenEvent and wx.EVT_FULLSCREEN.

* The legacy, OSX-Only wx.webkit module has been removed.

* Fix building wxPython with Python 3.10 on Windows (#2016)

* Fix PyProgress on Windows by avoiding invalid sizer flags (#1985)

* Fix 'More Grid Features' in demo

* Many of the widgets which deal with bitmaps have been changed to use a
  wx.BitmapBundle object instead of wx.Bitmap. This is the mechanism which
  wxWidgets has implemented for adapting to things like Hi-DPI displays.
  Essentially you can load a list of bitmaps of different sizes (but similar or
  scaled content) into a wx.BitmapBundle, and the widget can choose one based on
  the display density. Existing code should be able to continue to pass a
  wx.Bitmap to the widget constructor or to methods like SetBitmap, as wxPython
  will automatically convert from a wx.Bitmap to a wx.BitmapBundle containing
  the single image provided.

* Add support for new wx.grid event, EVT_GRID_ROW_MOVE

* Fix path issues in wx.lib.agw.multidirdialog (#2120)

* Fix eventwatcher checkAll(check=False) (#2139)

* Fix exception on grid labels click in 4.1.1a (#1841)

* Fix a large number of Python 3.10 issues.  In Python 3.10, a change was
  implemented where extension functions that take integer arguments will no
  longer silently accept non-integer arguments (e.g., floats) that can only be
  converted to integers with a loss of precision.  Fixed most of these issues
  in the pure-Python classes and demos by explicitly converting the parameters
  to int before passing them to wxWidgets.  There is loss of precision, but
  this was happening before (automatically) anyway as most wxWidgets
  DeviceContext functions operate using integers.

* Fix PlotCanvas point label drawing on Linux

* Fix GetPopupMenu override for wx.adv.TaskbarIcon (#2067)

* Fix invisible text in lib.plot with dark theme

* Add new button type: ShowHideToggleButton.  Like a ToggleButton, but with an
  associated "menu", a Window or Sizer which is shown/hidden when button is
  toggled. Includes methods for setting active and inactive fore/background
  colours.

* Fix unbinding of events in FIFO order (#2027)

* Enable customization of layout of pdfviewer button panel

* Support newer PyMuPDF versions (#2205)

* IntCtrl: Change default colour to wx.NullColour so the default color will be
  used. (#2215)

* Change PopupControl to respect all the parameters passed to its init method.
  (#2218)

* Fixes in flatmenu.py Remove and DestroyItem (#2219)

* Using the MinGW toolchain to build wxPython has been simplified a bit. (#2211)




4.1.1 "An attitude of gratitude"
--------------------------------
* 21-Nov-2020

PyPI:   https://pypi.python.org/pypi/wxPython/4.1.1
Extras: https://extras.wxPython.org/wxPython4/extras/
Pip:    ``pip install wxPython==4.1.1``

New and improved in this release:

* This should have been mentioned in the notes for the last release, but alas,
  it wandered away and got lost. wxWidgets is now validating the flags passed
  when adding items to a sizer, to ensure that they are the correct flags for
  the type of the sizer. If the given flags do not make sense, for example using
  horizontal alignment flags in a horizontal box sizer, then a wxAssertionError
  error is raised.

* Fixed missing binder for wxEVT_STC_AUTOCOMP_SELECTION_CHANGE. (#1613)

* DataViewModel.HasValue can be overridden and will inform the DataViewCtrl
  whether or not an item and column has data. If HasValue returns False, then
  GetValue for that item/col will not be called. This allows a distinction
  between a truly empty cell, and one that has a value even if it is an empty
  string. (#1600)

* Added flag that allows blocking of item dragging in the UltimateListControl
  class. (PR#1620)

* Add the column index to notification events in UltimateListControl (PR#1630)

* Added orientation parameter to UltimateListControl.GetScrollPos. (PR#1632)

* wx.lib.agw.aui.AuiNotebook RemovePage() now hides the removed page, so it
  needs to be shown again if it is reused in another place. (PR#1668)

* Fixed issue that could modify `bytes` objects under Python. (PR#1680)

* Added wx.lib.agw.aui.EVT_AUI_PANE_CLOSE event which is sent when a AUI (the
  agw version) Pane has been closed (after it has been closed, not when it is
  about to be closed, which is when EVT_AUI_PANE_CLOSE is sent.) (PR#1628)

* Exposed the wx.DC methods GetGraphicsContext and SetGraphicsContext. Depending
  on the platform and the type of the DC, there may be a wx.GraphicsContext used
  for the implementation of the DC. If so, the GetGraphicsContext method enables
  access to it. Be sure to check that the return value is not None before trying
  to use it.

* Simplified the implementation of the wx.App.InitLocale method. See the
  MigrationGuide for more information.

* Added wx.lib.agw.aui.AUI_DOCKART_HINT_WINDOW_BORDER_COLOUR constant
  so the hint window border color can be themed as well.

* The wx.lib.mixins.listCtrl.CheckListCtrlMixin is now obsolete because
  wx.ListCtrl has new functionality which does pretty much the same thing. In
  fact there is some overlap in method names which may trip up some use cases.
  It is advised to drop the use of CheckListCtrlMixin and just use the
  wx.ListBox functionality. You will need to call EnableCheckBoxes to turn it on,
  and you may need to change some event handlers or overloaded methods.

* wx.html2.WebView is now able to use Microsoft's Edge browser component as its
  backend renderer. This should improve the capabilities of the WebView widget
  on Windows, and be more consistent with the WebViews on the other platforms,
  compared to the original IE 11 backend. Using this backed requires that a
  new-ish version of the Edge browser is installed on the end user's computer.

* Added the wx.Image.ConvertToRegion method. This lets you create a wx.Region
  from an image and a specified color or the mask if the image has one. This
  was done to workaround a bug in wxMac, but it seems worthwhile enough to keep
  it around even after the bug was fixed.

* Added the missing context manager methods for wx.LogNull. (#1842)

* Refactored ScrolledThumbnail out of agw.ThumbnailCtrl so as to be usable
  outside of ThumbnailCtrl.



4.1.0 "Escaping the Quarantine"
-------------------------------
* 24-April-2020

PyPI:   https://pypi.python.org/pypi/wxPython/4.1.0
Extras: https://extras.wxPython.org/wxPython4/extras/
Pip:    ``pip install wxPython==4.1.0``

Starting with this release wxPython has switched to tracking the wxWidgets
master branch (version 3.1.x) for the wxWidgets source code, which wxPython is
built upon, and which is included in the wxPython source archives.

This will be the last release to include binaries for Python 2.7. The code will
likely still compile and be compatible with Python 2.7 for some time, but no
effort will be put into keeping it that way.


New and improved in this release:

* Add a sample for wx.Font.AddPrivateFont to the demo.

* Added wrappers for the OSXEnableAutomaticQuoteSubstitution,
  OSXEnableAutomaticDashSubstitution, and OSXDisableAllSmartSubstitutions
  methods in wx.TextCtrl. Also added OSXEnableAutomaticTabbing in wx.App.

* Added wx.ColourDialogEvent, wx.DCTextBgColourChanger, wx.DCTextBgModeChanger,
  wx.grid.GridCellDateRenderer, wx.grid.GridCellDateEditor, wx.SystemAppearance,
  etc.

* Many of the deprecated items in wxWidgets and wxPython are being or have
  been removed. Be sure to test your code in a recent 4.0.x release with
  warnings enabled so you can see which class, method or function calls you need
  to change.

* Bug fixes in wx.lib.calendar: key navigation across month boundaries is now
  possible; key navigation now sets the date and fires the EVT_CALENDAR event;
  setter APIs now set the date correctly (#1230).

* Switch to using a wx.Overlay in the Widget Inspection Tool to highlight
  widgets when running on a GTK3 port.

* Fixed issue in wx.lib.agw.customtreectrl where the label editor could remain
  stuck forever (#1235).

* Grafted on a EnableSystemTheme method to the classes which support it. This
  can be used to disable the default system theme on Windows for native widgets
  like wx.ListCtrl, wx.TreeCtrl and wx.dataview.DataViewCtrl. It has no effect
  on the other platforms.

* The wx.WS_EX_VALIDATE_RECURSIVELY extended style flag is obsolete, as it is
  now the default (and only) behavior. The style flag has been added back into
  wxPython for compatibility, but with a zero value. You can just stop using it
  in your code with no change in behavior. (#1278)

* Fix a sometimes crash when using a wx.Overlay by letting the wx.DCOverlay hold
  a reference to the DC, to ensure that the DCOverlay is destroyed first.
  (PR#1301)

* Replaced the Vagrant VMs used for building wxPython for various Linux distros
  with Docker images.

* Add some missing methods in wx.adv.BitmapComboBox (#1307)

* Added the wx.svg package which contains code for parsing SVG (Scalable Vector
  Graphics) files, and also code for integrating with wxPython. It can rasterize
  the SVG to a wx.Bitmap of any size with no loss of quality, and it can also
  render the SVG directly to a wx.GraphicsContext using the GC's drawing
  primitives. (PR #1323)

* Ported the embedding sample from Classic, which shows how to use wxPython from
  a C++ wxWidgets application that embeds Python. (PR #1353)

* Fixed wx.GetApp() to use wxWidgets' global wxApp instance instead of
  maintaining its own pointer. This way, if the wxApp is created by C++ code
  wxPython will still be able to get access to it. (#1126)

* Added wrappers for the wx.ActivityIndicator class.

* Added wrappers for the wx.CollapsibleHeaderCtrl class.

* Fixed issues in PlotCanvas around displaying and using scrollbars. (#1428)

* Added wx.msw.CHMHelpController, and also a wx.HelpController factory function
  that creates an instance of the best Help Controller for the platform. (#1536)

* Added wx.adv.GenericAnimationCtrl so the generic version of the animation classes
  can be used even on the platforms that have a native version. Note that due to
  internal changes to support both types of animations, some API changes in how
  the Animation objects are created. See the AnimationCtrl.py sample in the demo
  for the various usage patterns. (#1579)

* DataViewModel.HasValue can be overridden and will inform the DataViewCtrl
  whether or not an item and column has data. If HasValue returns False, then
  GetValue for that item/col will not be called. This allows a distinction
  between a truly empty cell, and one that has a value even if it is an empty
  string. (#1600)

* Added wrappers for the wx.grid.GridBlockCoords, wx.grid.GridBlocks, and
  wx.grid.GridBlockDiffResult classes, as well as associated new methods in the
  wx.grid.Grid class. These provide a new way to interact with blocks of
  selected cells, including an iterator interface in wx.grid.GridBlocks which
  should be a more efficient (time and memory) way to process large groups of
  selections.




4.0.7.post2 "To QTKit, or not to QTKit..."
------------------------------------------
* 12-Nov-2019

PyPI:   https://pypi.org/project/wxPython/4.0.7.post2
Extras: https://extras.wxPython.org/wxPython4/extras/
Pip:    ``pip install wxPython==4.0.7.post2``

This post-release changes a wxWidgets configure option on macOS so the build
will be forced to use AVFoundation instead of QTKit. This ensures that
wxMediaCtrl will work on macOS 10.15+, where all support for QTKit has been
removed.



4.0.7.post1 "Isn't it time for Python3?"
----------------------------------------
* 28-Oct-2019

PyPI:   https://pypi.org/project/wxPython/4.0.7.post1
Extras: https://extras.wxPython.org/wxPython4/extras/
Pip:    ``pip install wxPython==4.0.7.post1``

This post-release just fixes a problem with the numpy dependency constraint for
Python 2.7. (#1415)



4.0.7 "one more, for the road"
------------------------------
* 25-Oct-2019

PyPI:   https://pypi.org/project/wxPython/4.0.7
Extras: https://extras.wxPython.org/wxPython4/extras/
Pip:    ``pip install wxPython==4.0.7``

This release is comprised mostly of fixes and minor features which have been
back-ported from the master branch. This release is likely the last release of
the 4.0.x release series, and is certainly the last 4.0.x release that will
support Python 2.7. It may still continue to build for Python 2.7 for some time,
but no extra effort will be expended to keep it compatible.

This release provides the following changes:

* Bug fixes in wx.lib.calendar: key navigation across month boundaries is now
  possible; key navigation now sets the date and fires the EVT_CALENDAR event;
  setter APIs now set the date correctly (#1230).

* Switch to using a wx.Overlay in the Widget Inspection Tool to highlight
  widgets when running on a GTK3 port.

* Fixed issue in wx.lib.agw.customtreectrl where label editor could remain
  stuck forever (#1235).

* Fix a sometimes crash when using a wx.Overlay by letting the wx.DCOverlay hold
  a reference to the DC, to ensure that the DCOverlay is destroyed first.
  (PR#1301)

* Ported the embedding sample from Classic, which shows how to use wxPython from
  a C++ wxWidgets application that embeds Python. (PR #1353)

* Fixed wx.GetApp() to use wxWidgets' global wxApp instance instead of
  maintaining its own pointer. This way, if the wxApp is created by C++ code
  wxPython will still be able to get access to it. (#1126)

* Several other PRs have been backported from the master branch (which will
  become wxPython 4.1.0), the full list can be seen here:
  https://github.com/wxWidgets/Phoenix/pull/1357




4.0.6 "Applesauce"
------------------
* 21-May-2019

PyPI:   https://pypi.org/project/wxPython/4.0.6
Extras: https://extras.wxPython.org/wxPython4/extras/
Pip:    ``pip install wxPython==4.0.6``

This release provides the following fixes:

* Fixed a probably rare, but fatal bug on OSX when calling certain overloaded
  virtual methods with implementations in Python.

* Fixed char pointers in generated stub code to have a valid pointer value.

* Reverted the change that loads up install_requires from the contents of
  requirements.txt. Split the requirements.txt file into one for install and one
  for development.




4.0.5 "St. Helens Day"
----------------------
* 18-May-2019

PyPI:   https://pypi.org/project/wxPython/4.0.5
Extras: https://extras.wxPython.org/wxPython4/extras/
Pip:    ``pip install wxPython==4.0.5``

Changes in this release include the following:

* Added missing HtmlWindow.ScrollToAnchor method, and also a couple methods
  in HtmlCell too. (#1141)

* Added missing setters for the wheel-related properties in wx.MouseEvent.
  (#1140)

* Updated wxWidgets commit reference, bringing fixes for #1140, #1086 and
  #1147.

* Fix the use of the output parameter in HtmlWindow.OnOpeningURL the same way
  it was fixed in HtmlWindowInterface.OnHTMLOpeningURL. (#1068)

* Fixed a crashing bug when using a member of a transient wx.VisualAttributes
  object. Also set the attributes to be read-only to simplify the fix. (#1198).

* Updated the sip being used in wxPython builds to version 4.19.16.

* Added helper functions to check results of wxWidgets configure during the
  build of wxPython. Currently used to determine if the wx webview, glcanvas,
  and media libraries should be added to the link command. (#1138)

* Fixed scrollbar issue with ListCtrlAutoWidthMixin (#1215)

* Fixed file access in the wx.py and wx.tools.pywxrc packages to be Python 2 and
  3 compatible. (#1193, #1156)

* Fixes for building with Python 3.8 on Linux. (#1227)




4.0.4 "What? It's 2019 already?"
--------------------------------
* 5-Jan-2019

PyPI:   https://pypi.org/project/wxPython/4.0.4
Extras: https://extras.wxPython.org/wxPython4/extras/
Pip:    ``pip install wxPython==4.0.4``

Changes in this release include the following:

* Fixed an issue where wx.lib.intctrl would erroneously attempt to use long
  on Python3. (#898)

* Include the MSVC runtime DLLs for Python 3.7 builds too.

* Clear LIBPATH_PYEXT and LIB_PYEXT for linux builds too. (#904)

* Added a dependency on the Pillow package since it's used in some wx.lib.agw
  modules. (PR #908)

* Add flag to hide page in wx.lib.agw.aui.notebook. (#895)

* Switch wx.lib.plot to issue deprecation warnings with PlotPendingDeprecation
  so it doesn't have to enable all warnings to get them to be shown by default.
  (#902)

* Added a Python 3.7 builder on Fedora 28. (#925)

* Fix the object ownership transfer for wx.Menu.Insert() (#931)

* Added wx.Treebook.GetTreeCtrl, wx.Listbook.GetListView and
  wx.Choicebook.GetChoiceCtrl. (#918)

* Removed the wx.BookCtrlBase.RemovePage workaround as it was causing problems
  and doesn't seem to be necessary any more. The existing wxWidgets assertions
  are catching the out of range error just fine, however if wxWidgets was built
  without the debug helpers turned on then it could still cause a crash. (#888)

* Reverted the changes which removed the content of the wx.lib.pubsub package
  and encouraged users to switch to the real PyPubSub package instead. Removing
  it caused more issues than were expected so it has been restored and the code
  updated to PyPubSub v3.3.0. Version 4.0.0 is available upstream, but it is not
  compatible with Python 2.7. Now, wx.lib.pubsub is actually deprecated instead
  of just trying to pass control over to the upstream PyPubSub library. (#932)

* Improve calltip stability in pyshell. (#941)

* Fix TypeError in wx.lib.throbber. (#924)

* Fix missing parameter tool_id in
  wx.lib.agw.ribbon.toolbar.RibbonToolBar.AddToggleTool. (#947)

* Add a step to wx.Config.ReadInt to attempt converting from long to int
  under python2. (#384)

* Add virtual behavior for wx.RichTextCtrl and wx.TextCtrl's Copy/Cut/Paste methods
  and their Can* counterparts. (#954)

* Fix IO type in wx.lib.agw.thumbnailctrl  (#959)

* Fix type error that would occur using pycolourchooser. (#957)

* Optimize line drawing in HyperTreeList. (#973)

* Add wrapper for wx.StaticBox.GetBordersForSizer and use it in the demo to do
  platform-specific layout of the items in the StaticBox. (#974)

* Update wx.Point, wx.RealPoint, and wx.Size to use floating
  point arithmetic when conducting scalar multiplication (#971)

* Fix load/save bugs in PySlices (PR#978)

* Replace deprecated PIL.Image.tostring (PR#1005)

* Fix rendering and mouse sensitivity in UltimateListCtrl when adding HyperText
  items. (#1010)

* Added a parameter to lib.agw.CustomTreeCtrl.SetItemWindow(), to allow
  positioning the Window (a small image) on the left of text in a
  CustomTreeItem. (#PR886).

* Declared DeleteAllPages in the notebook subclasses, so the proper C++
  implementation will be called. (#972)

* Removed wx.lib.floatbar, which has been deprecated forever and probably
  hasn't been working in nearly as long. (#976)

* Updated SIP to version 4.19.13.

* Fix an issue in wx.lib.agw.aui.AuiManager where the orientation of
  an AuiToolBar would not be updated when calling LoadPerspective. (#917)

* Fixed a bug in wx.FileSystemHandler.OpenFile where the object ownership was
  not being transferred correctly, causing a crash after a premature object
  deletion. (#926)

* Fixed wx.ListCtrl.Append when wx.LC_SORT style is used, so appending items out
  of order does not lose the data for the remaining columns. (#906)

* Add wx.Accessible, it's Windows-only, will raise a NotImplementedError
  exception on the other platforms. (#958)

* Added the ability to generate stub classes for use when optional wxWidgets
  features are not part of the build. So far, stubs are available for
  wx.Accessible, wx.FileSystemWatcher, wx.glcanvas, wx.media and wx.html2.

* Moved the wxpy_api.h file into the wx package at wx/include/wxPython so it
  will be included in the wheel file. (#961)

* Fixed how string data is added to a virtual file-like object in
  wx.MemoryFSHandler. All strings are now added to the file as utf-8 encoded data,
  in both Python2 and Python3, and will be read from the virtual file the same
  way. If you need to use some other encoding for some reason you can first
  convert the text to a bytesarray or other buffer protocol compatible object and
  then create the virtual file from that data. (#969)

* Performance update for wx.lib.agw.customtreectrl (#1049)

* Ensure that colours set in wx.lib.agw.customtreectrl.TreeItemAttr are
  instances of wx.Colour. (#1032)

* Fix drawing of ticks in wx.lib.agw.speedmeter when there are negative bounds
  values. (#1013)

* wxWidgets for Mac includes the wxJoystick class now, also update the demo.
  (#997)

* Fix wx.html.HtmlPrintout to not be seen as an abstract class, so it can be
  instantiated. (#1060)

* Fix wx.aui.AuiNotbook.SetArtProvider to properly transfer ownership of the art
  object from Python to C++. This possible double-deletion and related crashing
  problems. (#1061)

* Fixed the wrappers for wx.html.HtmlWindow.OnOpeningURL to properly handle the
  redirect output parameter. (#1068) This is a backwards-incompatible change,
  please see the Migration Guide for details.

* TabNavigatorWindow works similarly to other programs now. It's resizable and
  draggable so if user has tons of files with long names, it isn't an irritation
  anymore plastered right in the middle of the screen and can't be worked with
  easily and ESC now cancels the popup with a proper returnId. (#1096)

* Added missing methods in wx.ListBox, SetItemForegroundColour,
  SetItemBackgroundColour and SetItemFont. (#1095)

* Backported a fix in wxWidgets that avoids crashing in hhctrl.ocx when using
  context sensitive help in 64-bit builds on Windows. (#1104)




4.0.3 "The show must go on. (Die show-stoppers! Die!)"
------------------------------------------------------
* 25-June-2018

PyPI:   https://pypi.org/project/wxPython/4.0.3
Extras: https://extras.wxPython.org/wxPython4/extras/
Pip:    ``pip install wxPython==4.0.3``

Changes in this release include the following:

* Fixed a linking problem on macOS. The new waf added an explicit link to the
  Python shared library which meant that it would try to load it at runtime,
  even if a different Python (such as Anaconda, EDM or Homebrew) was used to
  import wxPython. This, of course, caused runtime errors. (#892)

* Sort pages by dock_pos when added to automatic (agw.aui) notebook. (#882)

* Fix a bug in py.introspect.getTokens. (#889)

* Added Vagrant configuration for Fedora-28. Removed Fedora-23 (#884)

* Added wrappers for the wx.WindowIDRef class and added the wx.NewIdRef
  function. These will make it possible to create reserved Window IDs using the
  same mechanism which is used when passing wx.ID_ANY to a widget constructor.
  The object returned by wx.NewIdRef will automatically convert to an int when
  passing it to a window constructor, and can also be used as the source in a
  Bind(). (#896)

* Fixed issue when sys.prefix is not unicode (Python2) and when its contents
  are not translatable to utf-8.




4.0.2 "Cute as a June bug!"
---------------------------
* 16-June-2018

PyPI:   https://pypi.org/project/wxPython/4.0.2
Extras: https://extras.wxPython.org/wxPython4/extras/
Pip:    ``pip install wxPython==4.0.2``

Changes in this release include the following:

* Fixed wx.html2.EVT_WEBVIEW_NAVIGATING event not being sent on some versions
  of Linux. (#741)

* wx.Sizers can now be used as an iterator to iterate over the items within
  the sizer. (#738)

* Fix Python3 division in ThumbnailCtrl. (#746)

* Fix leaking image list in CheckListCtrlMixin (#752)

* All items marked as deprecated in the wxWidgets interface (documentation)
  files will now throw a DeprecationWarning when used from wxPython. Many of
  these items are disappearing in 4.1 so it's important to ensure they are
  deprecated at runtime too instead of just in the docs. (#749)

* Ensure that the attribute list given to the GLCanvas constructor is
  zero-terminated like it was in Classic. (#770)

* Updated to the wxWidgets 3.0.4 release version.

* Added the wxWidgets version number to the tail end of the string returned by
  wx.version().

* Bind EVT_WINDOW_DESTROY event only to the tree windows in CustomTreeCtrl,
  since otherwise it would be caught when child windows are destroyed too,
  which causes problems in this case. (#778)

* Fixed a problem where wx.TreeCtrl.OnCompareItems was not being called in
  derived classes on Windows. This was due to an optimization that wasn't
  compatible with how the classes are wrapped. (#774)

* Added wrappers for wx.ClassInfo and exposed wx.Object.GetClassInfo. This
  class is part of wxWidgets' internal type information system and although
  it is not very useful for Python applications it is useful for debugging
  some internal wxPython issues.

* Removed the wx.lib.pubsub package, and replaced it with code that imports
  the standalone PyPubSub in order remain compatible with older code that
  still uses wx.lib.pubsub. (#782, #792)

* Fixed bug in wx.lib.intctrl (#790)

* Fixed subclassing of wx.TextCompleter and wx.TextCompleterSimple (#827)

* Fixes for Python3 compatibility in PyCrust. (#823)

* Fix wxGet to be able to use pip v10. (#817)

* Change winid parameter in wx.ScrolledWindow to id, for consistency. (#816)

* Ensure that the page exists in book controls GetPage and RemovePage methods.
  At least one of the wx ports do not do this. (#830)

* Added missing wx.NumberEntryDialog

* Change wx.TextCompleterSimple.GetCompletions to send the list of strings
  as a return value, rather than a parameter that gets filled. (#836)

* Enabled the wx.GraphicsContext.Create(metaFileDC) wrapper (#811)

* Metafile support is also available on OSX, so wx.msw.Metafile and
  wx.msw.MetafileDC have been moved to the core wx module. So they can now be
  accessed as wx.Metafile and wx.MetafileDC.

* Updated the waf tool used by the build to version 2.0.7. This fixes problems
  with building for Python 3.7.

* Fixed alignment in buttons on MSW which have had foreground or background
  colors set. (#815)

* Fix for unexpected assertion inside wx.aui.AuiMDIChildFrame.Close.

* Fix a bug in setting AuiDockingGuide size. (#727)

* Remove unnecessary AUI notebook updating, and use wx.BufferedDC in Repaint()
  to mitigate flicker. (wx.lib.agw.aui). (#851, #686)

* Fixed crashing bug when using client data with items in
  wx.dataview.DataViewTreeCtrl. (#856)

* Detach wx.Control in AuiToolbar from current sizer before attach to a new
  one. (#843)

* Fixed a problem in wx.lib.mixins.listctrl.TextEditMixin where the height of
  the editor widget could be set to zero. (See discussion in #849)

* Fix a bug in calculating whether a tool fits into the AuiToolBar. (#863)

* Override SetForegroundColour and SetBackgroundColour in MaskedEditMixin (#808)

* Add an explicit wx.GraphicsContext.Create overload for wx.AutoBufferedPaintDC. (#783)

* Return original AGW window style in AuiToolBar.GetAGWWindowStyleFlag. (#870)

* Fix a bug in group management on wx.lib.masked.numctrl; the previous code used
  truediv ('/') to calculate _groupSpace, but in python 3.x this leads to a float
  result, instead of an integer as was expected. Using floordiv ('//') instead
  to solve the problem. (#865)

* Hide the window when the tool does not fit into AuiToolBar. (#872)

* Fixed the virtual dispatch code for the PGEditor.GetValueFromControl method
  to properly pass the parameters to the Python implementation, and also fixed
  how the return value is handled. (#742)

* Fixed all implementations of the PGProperty.StringToValue and IntToValue
  methods to treat the value parameter as a return value. (#742)

* Add missing wx.adv.EVT_CALENDAR_WEEK_CLICKED (#875)

* Fixed the stock labels to conform to Windows design guidelines. (#787)

* Always reset floating size and style when floating a toolbar in agw.aui. (#880)



4.0.1 "Lemonade"
----------------
* 2-Feb-2018

PyPI:   https://pypi.python.org/pypi/wxPython/4.0.1
Extras: https://extras.wxPython.org/wxPython4/extras/
Pip:    ``pip install wxPython==4.0.1``

This release is a quick hot-fix of some issues discovered in 4.0.0 just after
the release, plus a bit of  low-hanging fruit that was easy to squeeze in too.
Changes in this release include the following:

* A fix for a segfault that happens upon startup on newer linux releases. (#648)

* Set LD_RUN_PATH for the wxWidgets part of the build so the wx libs that are
  loaded by other wx libs can be found successfully. (#723)

* Use wxApp::GetInstance to check if there is an existing wxApp object. (#720)





4.0.0 "The Phoenix Takes Flight!"
---------------------------------
* 31-Jan-2018

PyPI:   https://pypi.python.org/pypi/wxPython/4.0.0
Extras: https://extras.wxPython.org/wxPython4/extras/
Pip:    ``pip install wxPython==4.0.0``

Changes in this release include the following:

* Fixes in wx.aui to properly transfer ownership of the menubar, and also some
  tweaks in the AUI_MDI sample in the demo. (#540)

* Added a wx.BUILD_TYPE value to distinguish between development, snapshot,
  and release builds. The value is also appended to wx.PlatformInfo. (Thanks
  Mesalu!)

* Fix crash when trying to fetch multiple items from a composite data object
  in wx.DropTarget.OnData. (#550) Also fixed the CustomDragAndDrop sample to
  not fail on Python 2.7.

* Add ability for wxArray wrappers to return a copy of the item in the
  ``__getitem__`` method. This solves problems where an array that is the
  return value of some method call is indexed immediately and a reference to
  the array is not held, which could result in garbage values for the indexed
  item. Currently this is turned on for just GridCellCoordsArray, but others
  can be switched in the future if needed. (#297)

* Add missing ``wx.GetLocale`` function. (#572)

* Add methods to wx.TextCtrl for output "file-like" compatibility. (#578)

* Fix object ownership issue for menus added to toolbar items. (#580)

* Updated SIP to version 4.19.5. One of the new features of this version is
  that integer overflows are no longer silently truncated and ignored. In
  other words, if a wrapped API has a parameter that is a C int type, and you
  pass a value that is larger than what will fit in that type of integer then
  an OverflowError exception will be raised.

* Fixed wx.richtext.RichTextBuffer.GetExtWildcard to return a tuple of 2
  values, as was done in Classic. (#594)

* Various fixes in UltimateListCtrl, HyperTreeList and CheckListCtrlMixin.
  (#592, #349, #612)

* Fixes in TextEditMixin to ensure that the new value is passed in the
  event. (#605)

* Fix comparing DataViewItem and TreeListItem objects with None. (#595)

* Fix event type name in wx/lib/sheet.py (#613)

* The wx.MessageDialog methods which take ButtonLabel parameters are now able
  to accept either strings or stock IDs. (#607, #276)

* Fix wx.EvtHandler.Unbind to work correctly when specifying the handler and
  it is a bound method. (#624)

* Fix OGL's ShapeCanvas to draw properly when the window is scrolled, and
  to also adjust the mouse coordinates, etc. (#635)

* Set a default background color for the generic buttons. (#651)

* Fixed HtmlWindow's OnFoo virtual methods so calls to them are propagated to
  the Python class. (#642)

* Fixed wx.CallLater to explicitly hold a reference instead of depending on an
  uncollectable cycle to keep the instance around. Like before the cycle is
  broken and the saved reference is deleted after the timer expires and the
  callable has been called. (#457)

* Although it's more or less just an implementation detail, add wrappers for
  wx.aui.AuiTabCtrl so references to it will get the correct type. (#664)

* List-like wrapper classes generated for accessing wxLists and wxArrays now
  support reverse indexing. (#669) For example::

      child = panel.GetChildren()[-1]


* Ported some of the classes in Classic's gizmos module from C++ to Python,
  including LEDNumberCtrl, DynamicSashWindow, and TreeListCtrl. The classes
  are now located in the wx.lib.gizmos package, with a compatibility module at
  the old wx.gizmos location. Please note that this TreeListCtrl class is a
  very different implementation than wx.dataview.TreeListCtrl, although there
  is some overlap in purpose. In addition, the new TreeListCtrl class is not
  actually a port from the old gizmos.TreeListCtrl but rather just a thin
  layer around AGW's HyperTreeList. This means that if you are using a non-
  default style flag you'll need to pass it to the agwStyle parameter instead
  of the style parameter.

* Fix crash when deleting all wx.dataview.TreeListCtrl items with wxGTK3.
  (#679, #704)

* Fix displaying '&' in the label of wx.RadioBox on GTK. (#39)

* Fix problems of the wrong C++ method being called in wx.ProgressDialog on MS
  Windows. (#701)

* Fixed how the scrollbar events are captured in DynamicSashWindow in order to
  fix regression in the sample. (#687)

* Allow extra CLI args to be passed to build.py by setting WXPYTHON_BUILD_ARGS
  in the environment.

* Added context manager methods to wx.DC that explicitly destroys the C++
  part of the DC upon exit. Using DCs as context managers is not required, but
  can be handy in the rare cases where something holds on to a DC for too
  long, perhaps unintentionally. (#680)

* Fixed crash due to too aggressive management of wxModules when we load
  subordinate extensions that have their own wxModules (wx.html, wx.adv, etc.)
  (#688)

* Fixed StyledTextCtrl.MarkerDefineRGBAImage and RegisterRGBAImage methods to
  be able to accept any Python buffer compatible object for the pixel data. (#716)





4.0.0b2 -- "Hurricanes, Floods, and Forest Fires! Oh My!"
---------------------------------------------------------
* 16-Sept-2017

PyPI:   https://pypi.python.org/pypi/wxPython/4.0.0b2
Extras: https://extras.wxPython.org/wxPython4/extras/
Pip:    ``pip install wxPython==4.0.0b2``

Changes in this release include the following:

* Added a deprecated compatibility helper for wx.CustomDataFormat.

* Transfer ownership of the wx.EvtHandler object when pushing/popping
  them, and also for Set/RemoveEventHandler. (#443)

* Add missing wx.VScrolledWindow methods listed in the docs as
  deprecated but still present. (#441)

* Fixed copy/paste error in wx.BusyInfo.__exit__ (#449)

* Added new tool wxget, (a minimal wx implementation of wget)

* Added new tools wxdocs and wxdemos to launch the respective items,
  fetching and unpacking as required. (#437)

* Fixes to ensure that the locale message catalogs are included in the
  release files. (#464)

* Fix wx.ListCtrl.SetItemData to check that the data value is not out
  of the range of a C long. (#467)

* Changed the default port on *nix builds to be GTK3. The new
  ``--gtk2`` flag for build.py can be used to force a build for GTK2
  instead, and the ``--gtk3`` flag still exists, but defaults to True
  unless ``--gtk2`` is specified. Please note that there is currently
  no auto-detection of whether GTK3 is available or not, so if you
  know you need to build for GTK2 then you need to use the build flag,
  and there is currently no way to specify that flag for builds
  performed by pip. (#431)

* Fix parameter names in Toolbar.AddTool methods to be
  consistent. (#475)

* Remove inconsistent GetVirtualSize method in ScrolledWindow and let
  it be inherited from wx.Window instead. (#474)

* Fix crashing bug caused by importing a module that reinitializes the
  wxModule system after having imported wxpyTag. (#468)

* Fix missing methods in various DataObject classes. (They were
  actually accidentally marked "private" when they should have been
  public.) (#480)

* Add missing ListCtrl.DeleteAllColumns. (#486)

* Various fixes in the demo.

* Fixed improper initial scale factor in wx.lib.agw.speedmeter

* Fix for calls to wx.Notebook.HitTest calling the wrong instance
  (base class version) of the method. (#499)

* Add wx.Simplebook class.

* Fix exception in wx.lib.agw.customtreectrl when calling
  SortChildren. (#463, #500)

* Fix missing imports needed for drawing the legend in
  wx.lib.plot. (#503)

* Fix other instances of list.sort using old cmp-style ordering
  functions.  (#508)

* Update SizedControls to do a sanity check on the parent's sizer, as
  GetSizer can return None for SizedParent under certain
  circumstances, such as when AUI reparents the control during pane
  movement. (#523, #537)

* Added Vagrant configs for Fedora 23 and Fedora 26, and dropped
  Fedora 24.  Wheels built on F23 can also be used on F24 and F25, and
  F26 adds Python 3.6 support.

* Fix bitwise OR bug in wx.lib.agw.aui.framemanager. (#493)

* Fix bugs in wx.lib.plot when saving file. (#526)

* Fix integer division bug in ultimatelistctrl. (#528)

* Fix bug in wx.SearchCtrl.SetCancelBitmap (#532)

* Fixed property grid SetPropertyValue method to not truncate floating
  point values to integers, and a couple other possible incorrect
  conversions.  (#536)





4.0.0b1
-------
* 22-July-2017

PyPI:   https://pypi.python.org/pypi/wxPython/4.0.0b1
Extras: https://extras.wxPython.org/wxPython4/extras/

Changes in this release include the following:

* Various little tweaks and fixes in some of the demo samples.

* Fixes in wx.lib.imagebrowser so it looks and acts better on OSX.

* Fixed problem due to wxModules not being initialized when non-core
  extensions are imported.

* Fixed issue in wx.TreeItemId comparison methods affecting PyCrust and
  other tools.

* Restore the simplified names for the wxGridSelectionModes enum that were
  present in Classic.

* Add accessors for the internal widgets in the wx.EditableListBox.

* Fixes in wx.lib.eventwatcher to avoid deprecated methods and other Phoenix
  related changes.

* Correctly transfer ownership of the input stream in wx.FSFile.

* Ensure the license files are getting into the source tarball and the
  binary wheel files.

* Add wrappers for the classes derived from wxImageHandler.

* Fix wx.lib.plot.polyline to not attempt to draw the spline if there are
  less than 3 points.

* Transfer the ownership of the prop arg in wx.propgrid.PGProperty.AddChild
  and AddPrivateChild. Various other fixes in wx.propgrid classes for
  backwards compatibility and to fix problems caused by mismatches between
  customizations that were done for Classic and how Phoenix does things by
  default. Also solved some problems in the PropertyGrid sample in the demo.

* Add missing HtmlCell.FindCellByPos.

* Enhance the DLG_UNIT convenience function such that if something other than
  a wx.Point or wx.Size was passed in then the return value will be a tuple.
  This eliminates some surprises that are possible due to auto-conversion of
  tuples to points or sizes.




4.0.0a3
-------
* 3-June-2017

Fixed a few cases where the GIL was not acquired before building tuples of
values. The problems associated with this (hangs or crashes) were sporadic and
seemingly random, and did not appear until there was a background thread that
was very busy. Running under a debug build of Python revealed the problem
almost immediately. Yay Python!

Return an integer value from wx.DC.GetHandle instead of a wrapped voidptr
object, similar to how it is done for wx.Window.GetHandle.

Make wx.TreeItemID hashable, with meaningful hash value and equality
operators, so it can be used as a dictionary key in Py3.

Fixed crash in wx.grid.GridTable.GetAttr, and potentially other cases of
classes derived from wx.RefCounter.

Add ShowPage and IsRunning methods to wx.adv.Wizard.

Fixed various GTK specific bugs and other cleanup in wx.lib.agw.aui.

Updated to SIP 4.19.2

Restored builders for Python 3.4 to the buildbot.

Restore the wrappers for GetPaperSize and SetPaperSize to wx.PrintData.

Fix crashing problem when a wx.TreeItemId was compared with None.

Fix for missing checkbox images in CheckListCtrlMixin on Linux and OSX.

Fix another crashing problem in propgrid, and a few other propgrid issues too.

The release version of the documentation can now be found at
https://docs.wxPython.org/ The documentation created during the
snapshot builds is still located at https://wxPython.org/Phoenix/docs/html/



4.0.0a2
-------
* 6-May-2017

This build of wxPython is based on the official wxWidgets 3.0.3 release.

This release is mostly various bug fixes and other tweaks, such as:

* Allow numpy arrays to be auto-converted to simple sequence value types like
  wx.Size, wx.Colour, etc.

* A couple of fixes to lib/agw/aui to prevent segfaults under OSX when
  AuiNotebook tabs are closed

* Fix wx._core.wxAssertionError in wx.lib.agw.aui when dragging a notebook tab

* Fix the [G|S]etClientData methods in wx.CommandEvent to behave the same
  way they are in wx.ClientDataContainer.

* Fix the SetFonts methods in wx.html classes

* Several fixes in wx.dataview related to overriding methods

* Fixed some flickering in wx.lib.agw.aui.framemanager

* Fixed problem with wrong implementation of wxNotebook::DeleteAllPages being
  called on Windows

* Added the missing wx.grid.GRID_AUTOSIZE flag

* Fixed crash due to the object created in an XmlSubclassFactory being
  destroyed too soon

* Fixed crash in wx.lib.agw.toasterbox

* Fixed crash when using wx.xrc.XmlSubclassFactory

* Fixed wx.grid.GridTableBase.GetValue and related methods to work more like
  they did in Classic, so non-string values can be used a little more
  easily.

Added building and bundling of the PDB files for wxWidgets and the wxPython
extensions on Windows.  Until a better place is found they will be
downloadable from https://wxPython.org/Phoenix/release-extras, along with
archives for the documentation as well as the demo and samples.




4.0.0a1  "The Phoenix Rises!"
-----------------------------
* 15-Apr-2017

This is the first official release of the wxPython Phoenix project! ("And the
crowd goes wild!") Don't let the fact that it is marked as an "alpha" release
scare you away. It is an alpha simply because this is the **first** in several
ways:

* It's the first real release of Phoenix, which is built on a different
  foundation than Classic wxPython was.

* It's the first wxPython release intended to be fully available from PyPI and
  buildable/installable by pip.

* It's the first release for Python 3.

* And there are still a few things that are not finished or polished yet.

But even with all that, many people have been using the pre-release snapshots
of Phoenix for quite a while now, and it has been relatively stable and solid
for them.

Due to some things being cleaned up, reorganized, simplified and dehackified
wxPython Phoenix is not completely backwards compatible with wxPython Classic.
This is intended. In general, however, the API differences tend to be minor
and some applications can use Phoenix with slight, or even no modifications.
In some other cases the correct way to do things was also available in Classic
and it's only the wrong way that has been removed from Phoenix.  For more
information there is a Migration Guide document available at:
https://wxpython.org/Phoenix/docs/html/main.html

The new wxPython API reference documentation, including all Python-specific
additions and customizations, and docs for the wx.lib package, is located at:
https://wxpython.org/Phoenix/docs/html/main.html




3.0.2.0
-------
* 28-Nov-2014

Fixed wxPython bug on OSX that was preventing the wx.App's virtual
methods related to handling App Events, like open-files or reopen-app,
from being handled correctly.

NOTE: It appears that wxPython applications on OSX will now always be
getting an initial Apple Event(s) sent to `MacOpenFiles` corresponding to
the name of the script and args on the python command-line.

Added patch #15142 which adds support for building with and using GTK3
as the wx platform.  Thanks kosenko!

Fixed the OSX Carbon build to actually use Carbon. (Because of a
change in defaults it was actually building the Cocoa build instead.)

Pythonized DataViewCtrl.HitTest.  It now takes just the Point parameter
and returns the DataViewItem and DataViewColumn objects. If there is
no item at that point then item will evaluate to False, (or you can
use its IsOk method.)  For example::

    item, col = ctrl.HitTest(point)
    if item:
        doSomething(item, col)





3.0.1.1
-------
* 9-Sept-2014

The previous release managed to escape out into the wild before the
3rdParty addons were updated from the source repository.  This release
includes the newest code from AGW and FloatCanvas which should have
been in the last release.

Fixed "wxPyHtmlWinTagHandler, no destructor found." error.



3.0.1.0
-------
* 6-Sept-2014

Turned on a workaround for a bug that caused crashes on Windows XP.
This was due to a Microsoft bug in optimizing access to TLS when a
DLL is dynamically loaded at runtime with LoadLibrary, such as how
Python extension modules are loaded.  See
http://trac.wxwidgets.org/ticket/13116

Fixed "wxPyXmlSubclassFactory, no destructor found." error.

Some Pubsub and AGW updates.

Ignore some code in wxOSX that was preventing stock data format IDs
from being used with custom data objects. (See
https://groups.google.com/forum/#!topic/wx-dev/wFxevpvbhvQ/discussion)

Various other fixes and enhancements from wxWidgets.



3.0.0
-------
* 25-Dec-2013

Merry Christmas (or your December holiday of choice)!

No new features but lots of bug fixes in wxWidgets and of course the
bump (finally!) up to 3.0.




2.9.5.0
-------
* 31-Aug-2013

wx.media.MediaCtrl on OSX-cocoa now has a functioning back-end using
the QTKit framework, so it works when running in either 32-bit or
64-bit mode.

Printing triggered from a Javascript window.print() statement will now
work on OSX when using the old wx.webkit or the new wx.html2 browser
controls.

Updated Scintilla code to version 3.21

Lots of fixes and improvements in the wxWidgets code.

Changed the wx.DateTime.Parse* methods to work like they did in
wxPython 2.8, they now return an integer indicating how far in to
the string that the parser parsed, or -1 on error.

Updated wx.lib.pdfviewer with patches from David Hughes.





2.9.4.1
-------
* 24-July-2012

A quick patch release to fix some C++ headers for the wxGTK port not
getting installed, causing a build error in wxPython.




2.9.4.0
-------
* 21-July-2012

wx.lib.pubsub: Pusub now defaults to the new "kwarg" version of the
API.  In order to continue using the original "arg1" API you will need
to import wx.lib.pubsub.setuparg1 before importing any other pubsub
modules.

The wx.RA_USE_CHECKBOX and wx.RB_USE_CHECKBOX constants were removed.
They were only used by the incomplete PalmOS port which has been
removed from the wxWidgets source tree.

wx.Font: There is now GetStrikethrough and SetStrikethrough methods.

wx.StaticBox: Fixed the client origin and client size on MSW so
children of the static box should not overlap the box's label or
border lines.

Added wx.HTMLDataObject

Applied a patch from Sam Partington that fixes some threading issues
in the wrapper code and other cool stuff.

Added the missing wx/lib/agw/data dir to the installers.

Add wx.EnhMetaFile and wx.EnhMetaFileDC for MSW.  This DC type is what
is used by the print framework in the print preview window, so it
needed to be wrapped so self.GetDC() would work properly.







2.9.3.1
-------
* 29-Dec-2011

Corrected some problems in the installer scripts that were not
including some new files.

Re-enabled the wrappers for the wx.GenericDatePickerCtrl class.

Applied some patches from Werner Bruhin for the sized controls classes
and demo, and which also adds the SizedScrolledPanel class.

Fixed several other minor bugs discovered in the last release.




2.9.3.0
-------
* 26-Dec-2011

wx.ListCtrl:  Added a static method named HasColumnOrderSupport which
returns a boolean value indicating if the column ordering APIs (see
next item) are implemented for the current platform.

Added methods for querying and manipulating the ordering of the
columns (in wx.LC_REPORT mode only.)  This is not implemented on all
platforms so use HasColumnOrderSupport to find out if the APIs are
supported.  The new APIs are: GetColumnOrder, GetColumnIndexFromOrder,
GetColumnsOrder and SetColumnsOrder.

Added wrappers for new WebView classes which came from a successful
Google Summer of Code project this year.  This new module allows you
to embed the platform's native HTML/CSS/Javascript rendering engine in
a wx application like we've always been able to do with wx.webkit on
Mac or with the various ActiveX modules that we've had for windows,
except in the new version it uses the exact same API on all platforms
and also provides an implementation for GTK.  Currently on Windows the
IE Trident engine is used, and WebKit is used on OSX and GTK.  The
code is organized to eventually allow alternate backend renderer
implementations.  The GTK version requires at least version 1.3.1 of
libwebkitgtk-dev, which is the default on most of the recent Linux
distributions.  Please note that although these new classes and
libraries are using names based on "WebView" I have put the wxPython
version of them in the wx.html2 module because the wxWebKit project
already produces a wx.webview module for wxPython.

The wx.lib.pubsub package has been updated to the latest version and
several examples have been added to the samples folder.




2.9.2.4
-------
* 9-Sept-2011

Try, try again...  Fixed an indentation bug that crept in somewhere
along the way.



2.9.2.3
-------
* 8-Sept-2011

Fixed a bug that was causing the base class methods of
wx.richtext.RichTextCtrl to be called incorrectly, causing a crash.



2.9.2.2
-------
* 5-Sept-2011

Fixed a problem with wx.ListCtrl.InsertStringItem when an imageIndex
was not passed.  Change the listctrl to not always assume that there
is an image.

Several fixes for the wx.lib.agw modules.

Fixed a problem in wxGrid on OSX-cocoa where it would close the cell
editor immediately because of extra kill focus events.

Added an OSX implementation for the wxRegion constructor taking a
sequence of points.

Added the ability to use the Cairo backend for wx.GraphicsContext on
Windows.  The Cairo libraries are loaded dynamically on-demand, so
there is not a runtime dependency on Cairo for applications that do
not use it.  The Cairo DLL and its dependencies are bundled with the
wxPython installers.  We expect to be able to also add dynamic loading
of Cairo for OSX soon, (but if anybody would like to volunteer that
would be nice too.)  To create a Cairo graphics context you first
have to get the Cairo GraphicsRenderer and then use it to create the
context, like this::

    cr = wx.GraphicsRenderer.GetCairoRenderer()
    ctx = cr.CreateContext(dc)

If either GetCairoRenderer or CreateContext fails (either it's not
supported or the Cairo shared libraries can not be found) then None
will be returned, so be sure to check the return values.  Using Cairo
on Windows is usually faster and seems to be of better quality than
using the GDI+ backend.

The wx.GCDC class can now be constructed with an already existing
wx.GraphicsContext.

The wx.lib.softwareupdate module has been added.  It implements a
class designed to be mixed with wx.App in a derived class and provides
code for enabling your applications to update themselves when new
releases are made available (very similar to how most applications on
the Mac will prompt you to allow it to self-update.)  This is based on
the Esky library available from the Python package index at
http://pypi.python.org/pypi/esky.  To enable your application to be
self-updatable it must be packaged as an Esky bundle, which is a .zip
file with a certain structure and meta-data, which means that you will
have to modify your setup.py files to enable this.  There is an
example showing how to do this in the samples/doodle folder of the
wxPython source tarball or the docs and demos package.

Added a MultiMessageDialog class to wx.lib.dialogs that is similar to
the stock wx.MessageDialog, but is additionally able to have a
scrollable message area, custom icons, and customized button labels,
(although they will still use the stock IDs).  There is also a
MultiMessageBox Function that is like the wx.MessageBox function.





2.9.2.1
-------
* 23-July-2011

Just before release of 2.9.2.0 an important bug was discovered in the
wxMSW printing code related to converting to and from native printer
definitions. To correct that glitch this .1 release was made with just
that one additional difference from the official wxWidgets 2.9.2
source tree.



2.9.2.0
-------
* (not released)

Added wx.CommandLinkButton.  This button has both a label and a note
displayed on it.  On Windows 7 it is a new native widget type, on the
other platforms it is a generic implementation using wx.Button.

Added wx.lib.itemspicker.  This class allows items to be selected from
a list by moving them to another list.

Added wx.UIActionSimulator, which is able to programmatically generate
platform specific keyboard and mouse events, (with varying degrees of
success depending on the platform.)

Added the ability to the build tools to make a Mac Framework for
wxWidgets, and use it in the wxPython build.  (We're still ironing out
some issues so it's not part of the release builds yet.)

Added an installer EXE for the wxWidgets source tree, including the
LIBs and DLLs that were used for the wxPython build on Windows.  This
enables 3rd party extension developers to build their libraries and
extensions such that they will use the same options and the same libs
as wxPython, and will replace the -devel tarball included with prior
releases.

There have been many improvements to the wxOSX-Cocoa port, making it
a more usable port.  The other ports have also improved as well.

The wx.TaskBarIcon in the wxOSX-cocoa port can now either be a custom
dock icon as before, or a status icon in the menu bar, and can be
selected by passing wx.TBI_DOCK or wx.TBI_CUSTOM_STATUSITEM to the
wx.TaskBarIcon constructor.  The default is menubar status item.  The
type flag is ignored on the other ports.

wx.ToggleButtons are now part of the new common button class hierarchy
and so they can now have bitmaps instead of or in addition to their
text labels.

Updates from the AGW and Editra projects.




2.9.1.1
-------
* 14-Oct-2010

wx.Bitmap:  Add ConvertToDisabled method.

wx.AboutBox: Added support for setting a long version string in
addition to the normal version string.

wx.App: Add ScheduleForDestruction, which will allow you to cause a
window to be destroyed sometime in the near future.  (Most likely to
be used to ensure that there are no more envents pending for the
widget.)

More methods and properties moved from wx.MouseEvent to the
wx.MouseState base class. Same for wx.KeyEvent and wx.KeyboardState,
which is used to hold modifier key states, and which is also a base
class of wx.MouseState.  Note that properties rightDown, leftDown and
middleDown have been changed to rightIsDown, leftIsDown and
middleIsDown.

wx.Button can now have both a text and a bitmap label (or just one or
the other.)  wx.BitmapButton is pretty much redundant and will likely
be phased out sometime in the future.  (The OSX Carbon build does not
support this new feature, but the Cocoa build does.)

wx.ComboBox:  Added Popup and Dismiss methods for programmatically
showing and hiding the popup, although they are not implemented for
all platforms yet.

wx.GenericDirCtrl can now select multiple paths.

Removed the deprecated wx.Effects class.

wx.Image: Added ConvertToGreyscale and ConvertToDisabled methods, also
new resampling scaling methods.

wx.Toolbar now supports inserting stretchable space between tools.

wx.Dialog can now be Window-modal or the usual App-modal.  On Mac this
results in the dialog sliding down in a sheet from the parent window's
top edge.  For platforms that don't support Window-modal dialogs it
will fall back to an App-modal behavior.  See
wx.Dialog.ShowWindowModal and the wx.Dialog sample in the demo.

wx.wizard.Wizard:  Add a new EVT_WIZARD_PAGE_SHOWN event.

Added wx.InfoBar, which is similar to the message bar used in some web
browser windows that is shown above or below the content window to
display messages and/or buttons in a way that doesn't interrupt the
user's workflow like a modal message dialog does, but is much more
noticeble than simply putting some text in the status bar.

Updated the Scintilla code used by wxStyledTextCtrl to version 2.03.

Added wx.GraphicsGradientStop[s] classes and updated the
Create*GradientBrush APIs to allow gradients with more than two color
stops.  Similar changes were also mare to the Cairo specific classes in
wx.lib.graphics to help maintain compatibility between the two.

Added the wx.lib.pdfviewer package which is a contribution from David
Hughes.  It implements a simple cross-platform PDF viewer widget using
the 3rd party pyPdf package for parsing the PDF file.  It's not super
fast nor is it feature complete, but for simple and small PDF files
(such as those produced by ReportLab) it works well.

Probably the most notable change in this release is the addition of
the OSX-Cocoa build, including a 64-bit architecture in the fat
binaries.  The Cocoa port requires at least OSX 10.5, and the Carbon
port requires 10.4 or better.  There are still some rough edges in the
Cocoa port, but a lot does work and works well.  If you run into
issues that seem to be Cocoa specific then be sure to create tickets
for them at http://trac.wxwidgets.org with the component set to
wxOSX-Cocoa, after having searched for any existing tickets for the
same issue of course.





2.9.0.1
-------
* 22-Jan-2010

NOTE: This release was done mainly to get a 2.9.x preview build out to
the wxPython contributors to use for testing their code with wxPython
2.9.  There will not be a general official release of this version.

NOTE: When using the stock Apple Python on OS X 10.6 it will default
to running in 64-bit mode if your machine is a 64-bit architecture.
wxPython is still using Carbon on OS X which is 32-bit only, so there
is no 64-bit personality in the universal binaries and it will raise
an exception when you import wx.  wxPython will be switching to Cocoa
soon, but in in the meantime you can force the stock Python to run in
32-bit mode by running this command in a Terminal session::

    defaults write com.apple.versioner.python Prefer-32-Bit -bool yes


wxGTK: Implemented support for underlined fonts in wx.StaticText

wxGTK: wx.TopLevelWindow.SetSizeHints size increments now work

Added wx.EventBlocker class

wxGTK: Make wx.TopLevelWindow.GetSize() return the size of the window
including the decorations (not just the client size) and updated
SetSize() to account for this as well.

wxMSW: For consistency with wxGTK, when a top level window is
minimized the size returned from GetSize will be the restored size,
not the size of the icon window.

wxGTK: For consistency with wxMSW, when a top level window is
minimized the size returned from GetClientSize will be (0,0).

wxGTK: Color cursors now supported.

Added wx.DC.StretchBlit() for wxMac and wxMSW (Vince Harron)

Added support for labels for toolbar controls (Vince Harron)

wxGTK: Setting foreground colour of single line wx.TextCtrl now works.

wxMac: Corrected top border size for wxStaticBox with empty label (nusi)

wx.Window.IsEnabled() now returns false even if the window parent, and
not the window itself, is disabled and added IsThisEnabled()
implementing the old IsEnabled() behaviour.

wxGTK: Now using the native tab traversal functions instead of
simulating it ourselves.

Generating wx.NavigationKeyEvent events doesn't work any more under
wxGTK (and other platforms in the future), use wx.Window.Navigate() or
NavigateIn() instead.

wx.glcanvas.GLCanvas: The constructor has been changed slightly in
order to make it consistent across all the platforms.  The C++ version
now looks like this::

    wxGLCanvas(wxWindow *parent,
               wxWindowID id = -1,
               const int *attribList = NULL,
               const wxPoint& pos = wxDefaultPosition,
               const wxSize& size = wxDefaultSize,
               long style = 0,
               const wxString& name = wxPyGLCanvasNameStr,
               const wxPalette& palette = wxNullPalette);

Also in GLCanvas, all the platforms now support the new pardigm of
using a separate GLContext object, and associating it with the canvas
using canvas.SetCurent(context).

wxMac: The get-url apple event is now supported, simply override
wx.App.MacOpenURL to receive it.  You'll also need to have appropriate
meta-data in your app bundle to specify the protocol of the URLs that
your app can respond to.

wx.VScrolledWindow has been refactored, and new wx.HScrolledWindow and
wx.HVScrolledWindow classes have been added.  Just like
wx.VScrolledWindow they allow scrolling with non-uniform scroll
increments, where the size of each item is determined by making
callbacks into the derived class.  The H version handles horizontal
scrolling and the HV version handles both horizontal and vertical
scrolling.

Support wx.APPLY and wx.CLOSE in CreateStdDialogButtonSizer()

wx.CheckListBox now looks more native, especially under XP.

Sizers distribute only the extra space between the stretchable items
according to their proportions and not all available space. We believe
the new behaviour corresponds better to user expectations but if you
did rely on the old behaviour you will have to update your code to set
the minimal sizes of the sizer items to be in the same proportion as
the items proportions to return to the old behaviour.

Added support for toolbar buttons with dropdown menus.

Added support for mouse events from two auxiliary mouse buttons.

The methods that wx.TextCtrl and wx.ComboBox have in common have been
factored out into a new base class that they share, wx.TextEntry.

wx.richtext.RichTextCtrl and related classes were refactored such that
the RTC uses the same attributes object as wx.TextCtrl.  This means that
instead of using wx.richtext.RichtextAttr or TextAttrEx you'll just
use wx.TextAttr instead.  Also, all of the flags and styles related to
the text attributes have been moved out of the wx.richtext module and
into the main wx namespace.  Finally, wx.TextCtrl and RichTextCtrl now
share some common base classes.

wx.Brush.MacSetTheme has been removed, and has been replaced by being
able to create a wx.Colour using a Mac themed brush ID instead.  So if
you used to have code like this::

    brush = wx.Brush(someColour)
    brush.MacSetTheme(kThemeBrushDialogBackgroundActive)

You'll want to replace it with code like this::

    brush = wx.Brush(wx.MacThemeColour(kThemeBrushDialogBackgroundActive))


wx.calendar:  A native implementation of the CalendarCtrl was added
for the Windows and GTK ports, however the native classes tend to not
implement all of the functionality that the old generic version of the
control provides.  To be able to provide a way for you to work around
issues related to this I've added wrappers for both the CalendarCtrl
and also GenericCalendarCtrl, so if you depend on the ability to do
things like set holidays or change the attributes of specific days in
the calendar then please change your code to use the GenericCalendarCtrl
class instead.

Added wx.NotificationMessage.

The wx.grid.GridCellEditor.EndEdit method has been split into two
methods, EndEdit and ApplyEdit.  See the GridCustEditor sample in the
demo for an example of their use.

Processing of pending events can be temporarily stopped and then
restarted.  See wx.App.SuspendProcessingOfPendingEvents and
ResumeProcessingOfPendingEvents.

Added wx.App.YieldFor and related methods which can control what
categories of events can be processed during the yield.

Spin buttons and spin controls now have their own event types instead
of reusing the scroll events.

The public data members of wx.MouseEvent (m_shiftDown, etc.) have been
removed, but since wx.MouseEvent now derives from wx.MouseState you
can use its properties (shiftDown, etc.) instead for assignments to
those member values.

Removed the Set/GetLogicalFunction methods from wx.GraphicsContext.

Added Set/GetCompositionMode methods to wx.GraohicsContext, and also
Set/GetAntialiasMode methods.  The composition mode settings allow you
to use the classic Porter-Duff compositions when drawing.  See
http://keithp.com/~keithp/porterduff/p253-porter.pdf

wx.grid.Grid:  Added methods CalcRowLabelsExposed,
CalcColLabelsExposed, CalcCellsExposed, DrawRowLabels, DrawRowLabel,
DrawColLabels, and DrawColLabel.

Added the wx.lib.mixins.gridlabelrenderer module.  It enables the use
of label renderers for Grids that work like the cell renderers do.  See
the demo for a simple sample.

wx.App:  OnExceptionInMainLoop and FilterEvent can now be overridden.

Added wx.lib.msgpanel, which provides a class derived from wx.Panel
that can look and feel much like a wx.MessageDialog.

Added wx.lib.progressindicator which is a simple class with a label
and a gauge that can be used to show either specific or indeterminate
(pulsed) progress of some sort.  It works well in status bars, and can
be set to hide itself when not active.

Added wx.lib.nvdlg, which provides a generic dialog for editing the
values of name/value pairs.  You're able to specify some styles and
attributes for each text control if needed.

Wrappers for the propgrid library, maintained by Jaakko Salli, have
been added to wxPython.

A new build script has been added to wxPython, originally created by
Kevin Ollivier, which greatly simplifies building both wxWidgets and
wxPython for the average user.  I now use it in my day-to-day builds
as well as from the scripts which create the preview and release
builds.  See the new BUILD.txt document for more information.





2.8.12.1
--------
* 23-July-2011

Relax an assert that was added to Bind() in the previous release so
None will be an acceptable value for the handler parameter again.

Added ToolTipString property to wx.Window.

Other minor fixes.

Updates from the AGW and Editra projects.



2.8.12.0
--------
* 16-April-2011

This release is mostly just bug and typo fixes.  There are no new
major features or enhancements in the core library.




2.8.11.0
--------
* 14-May-2010

Lots of bug fixes in both wxWidgets and wxPython.

Added the context manager protocol methods to some wx classes so they
can be used with the new Python 'with' statement.  (The with statement
is always available starting in Python 2.6, and can also be used in
Python 2.5 with a __future__ import statement.)  There are several
wx classes where this is a natural fit, such as wx.BusyInfo.  The
__enter__ and __exit__ methods have also been added to wx.Dialog where
it will do the dialog.Destroy() call for you.  This means that you can
use code like this::

    with MyDialog(self, foo, bar) as dlg:
        if dlg.ShowModal() == wx.ID_OK:
            # do something with dlg values

The list of wx classes that can now be used as context managers is:

* wx.Dialog
* wx.BusyInfo
* wx.BusyCursor
* wx.WindowDisabler
* wx.LogNull
* wx.DCTextColourChanger
* wx.DCPenChanger
* wx.DCBrushChanger
* wx.DCClipper

A new class has been added that is also a context manager, called
wx.FrozenWindow.  It will freeze the window passed to it upon entry to
the context, and will thaw the window upon exit from the context.

Applied the final version of patch #10959 to the PyCrust code.  It
adds many enhancements to the Py suite, including the ability to edit
blocks of code (called slices) as a whole before executing them, and
also the ability to execute some simple shell commands.

Replaced the wx.lib.pubsub module with the new pubsub package from
http://pubsub.sf.net.  By default it is backwards compatible with the
old pubsub module, but it also has a more advanced API available that
can be switched on at import time.  See the pubsub web site for more
details.

The wx.Effects class is deprecated.

Added Python 2.7 builds for Windows and Mac.

Added Debian package builds for Ubuntu 9.10 and 10.4.

Many fixes and enhancements for the wx.lib.agw package, including the
addition of pybusyinfo, ribbon, ultimatelistctrl and zoombar.





2.8.10.1
--------
* 14-May-2009

wx.grid.Grid:  Added methods CalcRowLabelsExposed,
CalcColLabelsExposed, CalcCellsExposed, DrawRowLabels, DrawRowLabel,
DrawColLabels, and DrawColLabel to the Grid class.

Added the wx.lib.mixins.gridlabelrenderer module.  It enables the use
of label renderers for Grids that work like the cell renderers do.  See
the demo for a simple sample.

Solved the manifests problem with Python 2.6 on Windows.  wxPython now
programmatically creates its own activation context and loads a
manifest in that context that specifies the use of the themable common
controls on Windows XP and beyond.  This also means that the external
manifest files are no longer needed for the other versions of Python.

wx.Colour: Updated the wx.Colour typemaps and also the wx.NamedColour
constructor to optionally allow an alpha value to be passed in the
color string, using these syntaxes:  "#RRGGBBAA" or "ColourName:AA"

wx.lib.wxcairo:  Fixed a problem resulting from PyCairo changing the
layout of their C API structure in a non-binary compatible way.  The
new wx.lib.wxcairo is known to now work with PyCairo 1.6.4 and 1.8.4,
and new binaries for Windows are available online at
http://wxpython.org/cairo/






2.8.9.2
-------
* 16-Feb-2009

Added the wx.lib.agw package, which contains most of the widgets from
http://xoomer.alice.it/infinity77/main/freeware.html written by Andrea
Gavana.  Andrea's widgets that were already in wx.lib were also moved
to the wx.lib.agw package, with a small stub module left in wx.lib.
As part of this addition the demo framework was given the ability to
load demo modules from a sub-folder of the demo directory, to make it
easier to maintain collections of demo samples as a group.

Added the wx.PyPickerBase class which can be used to derive new picker
classes in Python.  Used it to implement a color picker for Mac that
uses a wx.BitmapButton instead of a normal wx.Button.  This makes the
color picker look and behave lots better on Mac than before.

You can now pass the handler function to the Unbind method.  If it is
given then Unbind will only disconnect the event handler that uses the
same handler function, so if there are multiple bindings for the same
event type you'll now be able to selectively unbind specific
instances.

Added a new tool to the Widget Inspection Tool that allows you to watch
the events passing through a widget.  It can also be used
independently, see wx.lib.eventwatcher.





2.8.9.1
-------
* 28-Sep-2008

Fixed a Python 2.4 compatibility issue in the Editra code.




2.8.9.0
-------
* 28-Sep-2008

Many minor bug fixes throughout wxWidgets and wxPython.

Fixed wx.lib.embeddedimage to work with Python 2.3.

Fixed PseudoDC hit testing when pure white or pure black are used.

Added support for a 64-bit Windows build for the AMD64 architecture,
(a.k.a. x64.)  This is for Python 2.5 only and is available only as a
Unicode build.

Added the wx.EmptyBitmapRGBA factory function.

Added the wx.lib.wxcairo module which allows the pycairo package to be
used for drawing on wx window or memory DCs.  In addition it is able
to convert from a native wx.Font to a cairo.FontFace, and it also
provides functions for converting to/from wx.Bitmap and
cairo.ImageSurface objects.  In order to use this module you will need
to have the Cairo library and its dependencies installed, as well as
the pycairo Python package.  For Linux and other unix-like systems you
most likely have what you need installed already, or can easily do so
from your package manager application.  See the wx.lib.wxcairo
module's docstring for notes on where to get what you need for Windows
or Mac.  This module uses ctypes, and depending on platform it may
need to find and load additional dynamic libraries at runtime in
addition to cairo.  The pycairo package used needs to be new enough to
export the CAPI structure in the package namespace.  I believe that
started sometime in the 1.4.x release series.

Added the wx.lib.graphics module, which is an implementation of the
wx.GraphicsContext API using Cairo (via wx.lib.wxcairo).  This allows
us to be totally consistent across platforms, and also use Cairo to
implement some things that are missing from the GraphicsContext API.
It's not 100% compatible with the GraphicsContext API, but probably
close enough to be able to share code between them if desired, plus it
can do a few things more.

Updated wx.Bitmap.CopyFromBuffer to be a bit more flexible. You can
now specify the format of the buffer, and the CopyFromBufferRGBA is
now just a wrapper around CopyFromBuffer that specifies a different
format than the default.  Also added the complement method,
CopyToBuffer.  See the docstring for CopyFromBuffer for details on the
currently allowed buffer formats.  The existing wx.BitmapFromBuffer
factory functions are also now implemented using the same underlying
code as CopyFromBuffer.

Add wx.lib.mixins.listctrl.ListRowHighlighter for automatic highlighting
of rows in a wx.ListCtrl.



2.8.8.1
-------
* 18-July-2008

wx.richtext: Added wrappers for the RichTextPrinting and
RichTextPrintout classes.

Make it easier to replace the check box images used in the
CheckListCtrlMixin class.

Fixed bug in wx.ScrolledWindow when child focus events caused
unnecessary or incorrect scrolling.

Fixed a bug in wx.GridBagSizer where hidden items were not ignored in
part of the layout algorithm.

Several other bugs also fixed.




2.8.8.0
-------
* 23-June-2008

Added the PlateButton class from Cody Precord.

Added wx.PyEvtHandler, which supports overriding the ProcessEvent
method in derived classes.  Instances of this class can be pushed onto
the event handler chain of a window in order to hook into the event
processing algorithm, and its ProcessEvent method will be called for
every event sent to the window.

With much help from Anthony Tuininga the code generated by the img2py
tool is now cleaner, simpler and smaller.  Instead of writing the data
for the images as printable ascii with hex escapes it now uses base64
to encode the images into a string.  In addition, instead of top-level
functions for returning the image data and bitmaps, the embedded
images now use a simple class with methods for returning the image as
a bitmap, icon, or etc.  By default in 2.8.x top-level aliases will be
generated to make the code backward compatible with the old functional
interface, but you can use -F to turn that off.  In 2.9 and beyond the
default will be to generate only the new class interface, but -f can
be used to turn the old behavior back on.

The PyEmbeddedImage class added for the new img2py support can also be
used for image data that may be acquired from some other source at
runtime, such as over the network or from a database.  In this case
pass False for isBase64 (unless the data actually is base64 encoded.)
Any image type that wx.ImageFromStream can handle should be okay.  See
the wx.lib.embeddedimage module for details.

Exposed the wx.GenericDatePickerCtrl to wxPython.  On wxGTK and wxMac
this is exactly the same as the normal date picker, but on wxMSW it
allows you to avoid the native wx.DatePickerCtrl if so desired.  Also
fixed a bug that caused an assert if you tried to set the date to
wx.DefaultDateTime even if wx.DP_ALLOWNONE was specified.

Made a little hack in wx.lib.masked.TextCtrl that allows it to be
wrapped around an already existing TextCtrl instead of always creating
its own.  This is useful for example with the wx.TextCtrl that is
built-in to the customizable wx.combo.ComboCtrl, or with a textctrl
that is part of an XRC layout.  To use it you need to do a little
trick like this::

       existingTextCtrl = combo.GetTextCtrl()
       maskedCtrl = wx.lib.masked.TextCtrl.__new__(wx.lib.masked.TextCtrl)
       maskedCtrl.this = existingTextCtrl.this
       maskedCtrl.__init__(parent)

Enhanced the Widget Inspection Tool with some new functionality.
Added tools to the toolbar to expand and collapse the widget tree,
which is very helpful for not getting lost in very large applications
with many hundreds of widgets.  Also added a toolbar tool for
highlighting the currently selected widget or sizer in the live
application.  The tool will flash top-level windows and for all other
items it will draw an outline around the item for a few seconds.

Copied the sized_controls module to the wx.lib package as the first
step of phasing out the wxaddons package.

Added an implementation of wx.Window.SetDoubleBuffered on Windows.
(GTK already has one, and Mac doesn't need one because everything is
always double buffered by the system there.)

Added a wrapper to wx.TopLevelWindow for MacGetTopLevelWindowRef to
facilitate calling the Carbon APIs directly for things that are not
supported in wx, similar to how we can use ctypes or PyWin32 with
window.GetHandle() to do custom stuff on Windows.  (On wxMac GetHandle
returns the ControlRef, which is different than the WindowRef, hence
the need for a 2nd method.)  Here is an example to set the modified
flag in the caption::

    >>> import ctypes
    >>> carbon = ctypes.CDLL('/System/Library/Carbon.framework/Carbon')
    >>> carbon.SetWindowModified(frame.MacGetTopLevelWindowRef(), True)


Added a new light-weight solution for embedding ActiveX controls in
wxPython applications that uses ctypes and the comtypes package
available from http://starship.python.net/crew/theller/comtypes/.
Comtypes allows us to use and provide an interface with full dynamic
dispatch abilities, much like PyWin32's COM interfaces but with much
reduced external dependencies.  See wx/lib/activex.py for more
details.  IMPORTANT: Be sure to get at least version 0.5 of comtypes,
see the docstring in the wx.lib.activex module for details.

The wx.lib.iewin, wx.lib.pdfwin, and wx.lib.flashwin modules were
switched to use the new and improved activex module.  The APIs
provided by these modules should be mostly compatible with what was
there before, except for how the COM events are handled.  Instead of
sending wx events it relies on you overriding methods with the same
names as the COM events.  You can either do it in a or derived class,
or you can set an instance of some other class to be the event sink.
See the ActiveX_IEHtmlWindow sample in the demo for an example.  If you
would rather continue to use the old version of these modules they
are available in the wx.lib with "_old" added to the names.

Added the wx.lib.resizewidget module.  This module provides the
ResizeWidget class, which reparents a given widget into a specialized
panel that provides a resize handle for the widget. When the user
drags the resize handle the widget is resized accordingly, and an
event is sent to notify parents that they should recalculate their
layout.





2.8.7.1
-------
* 29-Nov-2007

Applied Patch [ 1783958 ] to use the native renderer for drawing the
checkboxes in CheckListCtrlMixin.

Incorporated the new version of XRCed.  This is the result of a Google
Summer of Code 2007 project by Roman Rolinsky, and includes a number
of UI enhancements, as well as a mechanism for adding support for new
components without needing changes to XRCed itself.  These new
components can be those supported at the C++ layer of XRC, as well as
custom XRC handlers written in Python.  See
http://wiki.wxpython.org/XRCed_Refactoring_Project

wxMac: Fixed wx.BusyInfo so it doesn't steal the activated status
from the parent window.  (This actually applies to all frames with the
wx.FRAME_TOOL_WINDOW style and no decorations.)

wxMac: Fixed the lack of painting the area between scrollbars on
Leopard.

wxMac: Fixed assertion errors dealing with toolbars on Leopard.

wxMac: Multiline textcontrols now support attributes for margins and
alignment; only a single tab distance can be set though.

Added the wx.Image.AdjustChannels method.  This function muliplies all
4 channels (red, green, blue, alpha) with a factor (around
1.0). Useful for gamma correction, colour correction and to add a
certain amount of transparency to a image.

Added Editra to the distribution, to give us a simple yet powerful
programmer's code editor to replace the never finished PyAlaMode
editor and related tools.  Many thanks to Cody Precord for the work he
has done on this tool and for allowing us to make it part of wxPython.
Editra has syntax highlighting and other support for over 40
programming languages, excellent OS X integration, is extendable via
plugins, and for those that are on the VI side of the fence there is a
VI emulation mode.  For more information see the Editra website at
http://editra.org/

wxGTK: wx.Frame.ShowFullScreen now preserves the menubar's
accelerators.

wxGTK: wx.GetClientDisplayRect fixed.

Applied patch [1838043], which adds a demo of the wx.RendererNative
class functionality.

Applied patch [1837449], which uses wx.RenderNative for drawing the
combo button in the PopupControl.

Added GetDirItemData to wx.GenericDirCtrl, which returns a reference
to the data object associated with an item in the control.  (Patch
#1836326)





2.8.6.1
-------
* 26-Oct-2007

wxMac: Fixed paste bug when the clipboard contains unicode text.

AUI: Added missing event binders for the notebok tab events.

wxMac: Fixed bug that resulted in portions of virtual listctrl's to
not be repainted when scrolling with PgUp/PgDown/Home/End.

wxMac: Fixed bug that broke tab traversal when tabbing runs into a
wx.StaticBox.

wxGTK:  Add wx.Window.GetGtkWidget.

All: Undprecated wx.ListCtrl.[G|S]etItemSpacing

All: Fixed wx.Palette constructor wrapper.  It takes three sequences of
integers to specify the R, G, and B values for each color in the
palette, which must all be the same length and which must contain
integer values in the range of 0..255 inclusive.

Thanks to some grunt work from Edouard TISSERANT, wxPython now has the
needed tweaks in config.py to be able to be built with mingw32.  See
BUILD.txt for details.

Changes in wx.GraphicsContext to make things like the half-pixel
offsets more consistent across platforms.

wxMSW: If freezing a top-level window wxWidgets will actually freeze
the TLW's children instead.  This works around a feature of MS Windows
that allowed windows beneath the frozen one in Z-order to paint
through, and also mouse events clicking through to the lower window.





2.8.6.0
-------
* 27-Sept-2007

This release is mostly about fixing a number of bugs and
inconsistencies in wxWidgets and wxPython.  In other words, there have
been a whole lot more changes than what is listed here, but they are
not new features or API visible changes, which is what are usually
listed in this file.

Some Menu APIs added to make things more consistent.  Added
wx.MenuBar.SetMenuLabel, wx.MenuBar.GetMenuLabel,
wx.MenuBar.GetMenuLabelText, wx.Menu.GetLabelText,
wx.MenuItem.SetItemLabel, wx.MenuItem.GetItemLabel,
wx.MenuItem.GetItemLabelText, wx.MenuItem.GetLabelText.  The
Get...Label functions get the raw label with mnemonics and
accelerators, and the Get...LabelText functions get the text only,
without mnemonics/accelerators.

Added wx.BORDER_THEME style.  This style will attempt to use a theme
specific style, if the current platform and environment is themeable
and has a specific theme style.  For example, you could use this on
Windows XP on a custom control to give it a themed border style that
looks like what is used by default on the native wx.TextCtrl or
wx.ListBox.  Since there were not any more available bits for border
styles, this style replaces wx.BORDER_DOUBLE.






2.8.4.2
-------
* 8-Aug-2007

Added some SWIG magic that allows wx C++ lists to be exposed to
wxPython as sequence-like wrappers around the real list, instead of
making a Python list that is a copy of the real list as was done
before.  These sequence-like objects support indexing, iteration,
containment tests ("obj in seq") and index(obj), but not anything that
would modify the sequence.  If you need to have a real list object
like before then you can pass the sequence to Python's list() function
to convert it.  Current functions that are affected by this are
wx.Window.GetChildren, wx.GetTopLevelWindows, wx.Sizer.GetChildren,
and wx.Menu.GetMenuItems.  Care should be taken to be sure that you
don't try to use the sequence after the C++ object the list belongs to
has been destroyed.

Updated wrappers for the RichTextCtrl classes that were already
wrapped, and added support for loading rich xml files and saving as
HTML or XML.

Added wxRoses sample from Ric Werme.

Added better wrappers for wx.OutputStream and wxPython now deals with
them similarly to how it handles wx.InputStreams.  Specifically, any
Python file-like object can be passed where a wx.OutputStream is
expected and the data will be written to the file object
appropriately.

Added some patches from Billy B. that improve the pySketch sample.

Added patch from Chris Mellon that gives PyShell a custom context
menu that is better integrated with the shell environment.

There are now new build scripts for making the Universal binaries and
Installer for OS X.  There is no longer any need for separate builds
for each OS version, all builds are now Universal and work on both
Panther and Tiger, and on PPC and i386.

On the Linux side the debian and ubuntu packages will support multiple
versions of Python if the Debian/Ubuntu release is set up to support
more than one version.  To check which versions you can expect to get
you can run "pyversions -s".  Also there is a new package available
that contains a debug version of the wxPython extension modules, that
can be used with the python-dbg package.  In addition the RPMs are now
being built for Fedora Core 6 and Fedora Core 7.





2.8.4.0
-------
* 14-May-2007

wxGTK: Make wx.NO_BORDER style work with wx.RadioBox (patch 1525406)

Update to 1.0 of TreeMixin.

wx.lib.customtreectrl: Patch from Andrea that fixes the following
problems/issues:

* ZeroDivisionError when using the Vista selection style and calling
  SelectItem; for some strange reason, sometimes the item rect is
  not initialized and that generates the ZeroDivisionError when
  painting the selection rectangle;

* Added a DeleteWindow method to GenericTreeItem class, for items
  that hold a widget next to them;

* Renamed CustomTreeCtrl method IsEnabled to IsItemEnabled, otherwise
  it conflicts with wx.Window.IsEnabled;

* Now CustomTreeCtrl behaves correctly when the widget attached to an
  item is narrower (in height) than the item text;


wx.lib.flatnotebook: Patch from Andrea that implements the following:

* A new style FNB_FF2: my intentions were to make it like Firefox 2,
  however it turned out to be an hybrid between wxAUI notebook glose
  style & FF2 ...I still think it looks OK. The main purpose for
  making it more like wxAUI is to allow applications that uses both
  to have same look and feel (or as close as it can get...);

* Changed the behavior of the left/right rotation arrows to rotate
  single tab at a time and not bulk of tabs;

* Updated the demo module.

XRCed now uses a wx.FileHistory object for managing the recent files
menu.

wx.DateSpan and wx.TimeSpan now use lower case property names in order
to not conflict with the same named static methods that already
existed.

wx.aui.PyAuiDocArt and wx.aui.PyAuiTabArt can now be derived from in
wxPython and plugged in to wx.AUI.

XRCed has a new experimental feature to add controls by dragging icons
from the tool palette to the test window. Mouse position is tracked
to highlight the future parent of the new item.

Updates to MaskedEdit controls from Will Sadkin:

maskededit.py:
  Added parameter option stopFieldChangeIfInvalid, which can be used to
  relax the validation rules for a control, but make best efforts to stop
  navigation out of that field should its current value be invalid.  Note:
  this does not prevent the value from remaining invalid if focus for the
  control is lost, via mousing etc.

numctrl.py, demo / MaskedNumCtrl.py:
  In response to user request, added limitOnFieldChange feature, so that
  out-of-bounds values can be temporarily added to the control, but should
  navigation be attempted out of an invalid field, it will not navigate,
  and if focus is lost on a control so limited with an invalid value, it
  will change the value to the nearest bound.

combobox.py:
  Added handler for EVT_COMBOBOX to address apparently inconsistent behavior
  of control when the dropdown control is used to do a selection.

textctrl.py
  Added support for ChangeValue() function, similar to that of the base
  control, added in wxPython 2.7.1.1.

Update to latest FloatCanvas from Chris Barker.

The pywxrc tool now properly supports generating classes for menus and
menubars, and also creating attributes for menus, menubars and menu
items.





2.8.3.0
-------
* 22-March-2007

Added wx.ToolBar.SetToolNormalBitmap and SetToolDisabledBitmap
methods.  (Keep in mind however that the disabled bitmap is currently
generated on the fly by most native toolbar widgets, so this
SetToolDisabledBitmap method won't have any affect on them...)

Refactored the inspection tool such that it can be used as a wx.App
mix-in class as it was used before (with the wx.lib.mixins.inspect
module) and also as a non mix-in tool (using wx.lib.inspect.InspectionTool).

Add wx.lib.mixins.treemixin from Frank Niessink.

Added the wx.SizerFlags class, and also added AddF, InsertF and
PrependF methods to wx.Sizer.  The wxSizerFlags class provides a
convenient and easier to read way to add items to a sizer.  It was
added as a new set of methods of the wx.Sizer class so as to not
disturb existing code.  For example, instead of writing::

    sizer.Add(ctrl, 0, wx.EXPAND | wx.ALL, 10)

you can now write::

    sizer.AddF(ctrl, wx.SizerFlags().Expand().Border(wx.ALL,10))


Will Sadkin provided a patch for the wx.lib.masked package that fixes
its support for using the navigation keys on the numeric keypad.

wx.lib.plot: patch #1663937 to allow user to turn off scientific
notation on plot.

wxGTK: Most of the remaining TODOs for the wx.GraphicsContext on wxGTK
have been done.  This includes implementations for GetTextExtent,
Clip, DrawBitmap, fixing the drawing position of text to be at the
upper left corner instead of the baseline, etc.

wx.lib.customtreectrl patches from Andrea:

1. ExpandAll has been renamed as ExpandAllChildren, and the new
   ExpandAll now takes no input arguments (consistent with
   wx.TreeCtrl)

2. ctstyle keyword is now defaulted to 0: every style related to
   CustomTreeCtrl and the underlying wx.PyScrolledWindow should be
   declared using the keyword "style" only. For backward
   compatibility, ctstyle continues to work as I merged ctstyle and
   style in the __init__ method.

3. GetClassDefaultAttributes is now a classmethod.

4. UnselectAll bug fixed.


Renamed the wx.lib.inspect and wx.lib.mixins.inspect modules to
inspection, in order to avoid conflicts with the inspect module in the
standard Python library.

Lots of changes to XRCed from Roman Rolinsky:

*  Preferences for default "sizeritem" parameters for new panels and
   controls can be configured ("File">"Preferences...").

*  Implemented comment object for including simple one-line comments and
   comment directives as tree nodes. No validation is performed for a
   valid XML string so comments must not contain "-->". Comment directive
   is a special comment starting with '%' character, followed by a line
   of python code. It is executed using 'exec' when the resource file is
   opened. This is useful to import plugin modules containing custom
   handlers which are specific to the resource file, however this is of
   course a security hole if you use foreign XRC files. A warning is
   displayed if the preference option 'ask' is selected (by default).

*  Added support for custom controls and plugin modules. Refer to this
   wxPythonWiki for the details:  http://wiki.wxpython.org/index.cgi/XRCed#custom

*  Tool panel sections can be collapsed/expanded by clicking on the
   label of a tool group.

*  Some undo/redo and other fixes.

*  Fixes for wxMSW (notebook highlighting, control sizes, tree Unselect).

*  Notebook page highlighting fix. Highlight resizes when the window
   is resized. ParamUnit spin button detects event handler re-entry
   (wxGTK probably has a bug in wxSpinButton with repeated events).

*  Fix for dealing with empty 'growable' property, using MiniFrame
   for properties panel, the panel is restored together with the
   main window.





2.8.1.1
-------
* 19-Jan-2007

wxMSW: Fix lack of spin control update event when control lost focus

Added a typeId property to the PyEventBinder class that holds the
eventType ID used for that event.  So when you need the eventType
(such as when sending your own instance of standard events) you can
use, for example, wx.EVT_BUTTON.typeId instead of
wx.wxEVT_COMMAND_BUTTON_CLICKED.   Note that there are a few composite
events, such as EVT_MOUSE and EVT_SCROLL, that will actually bind
multiple event types at once, and in these cases the typeId property
may not give you what you want.  You should use the component events in
these cases.

PyCrust now has an option for showing/hiding the notebook.

wxMSW:  Corrected drawing of bitmaps for disabled menu items.

Enhanced the wx.lib.mixins.inspect module.  In addition to showing a
PyCrust window it is now a widget browser, which provides a tree
loaded up with all the widgets in the app, optionally with the sizers
too, and also a panel displaying the properties of the selected
window.  Run the demo and type Ctrl-Alt-I keystroke (or Cmd-Alt-I on
the Mac) to see how it works.  You can add this to your own apps with
just a few lines of code.

Added wx.SearchCtrl.[Get|Set]DescriptiveText

wxMac: Added support for the wx.FRAME_FLOAT_ON_PARENT style.

wxMac: the popups used for call tips and autocomplete lists in
StyledTextCtrl (such as in PyShell) are now top-level float-on-parent
windows so they are no longer clipped by the bounds of the stc window.





2.8.1.0
-------
* 8-Jan-2007

Added EVT_TASKBAR_CLICK and use it to show taskbar icon menu on right
button release, not press, under MSW (bug 1623761)

Added wx.TreeCtrl.CollapseAll[Children]() and IsEmpty() methods

Fix wx.MDIChidFrame.GetPosition() (patch 1626610)

Fix attribute memory leak in wx.grid.Grid::ShowCellEditControl() (patch
1629949)

wxGTK: Fix for controls on a toolbar being the full height of the
toolbar instead of their natural height.

wx.lib.customtreectrl patches from Andrea Gavana.

wxMac: Applied patch #1622389, fixing two memory leaks in
GetPartialTextExtents.

More fixes for the native wx.ListCtrl on Mac.

Added wx.aui.AuiNotebook.GetAuiManager().

Added wx.aui.AuiMDIParentFrame and wx.aui.AuiMDIChildFrame, which
essentially implement the MDI interface using a normal wx.Frame and a
wx.aui.AuiNotebook.




2.8.0.1
-------
* 11-Dec-2006

Lots of fixes and updates to the AUI classes.

Added wx.CollapsiblePane.  On wxGTK it uses a native expander widget,
on the other platforms a regular button is used to control the
collapsed/expanded state.

Added the wx.combo module, which contains the ComboCtrl and ComboPopup
classes.  These classes allow you to implement a wx.ComboBox-like
widget where the popup can be nearly any kind of widget, and where you
have a lot of control over other aspects of the combo widget as well.
It works very well on GTK and MSW, using native renderers for drawing
the combo button, but is unfortunately still a bit klunky on OSX...

Use system default paper size for printing instead of A4 by default.

Added wx.combo.OwnerDrawnComboBox, which is a ComboCtrl that delegates
the drawing of the items in the popup and in the control itself to
overridden methods of a derived class, similarly to how wx.VListBox
works.

Added wx.combo.BitmapComboBox which is a combobox that displays a
bitmap in front of the list items.

Added the wx.lib.mixins.inspect module.  It contains the InspectMixin
class which can be mixed with a wx.App class and provides a PyCrust
window that can be activated with a Ctrl-Alt-I keystroke (or Cmd-Alt-I
on the Mac.)

Added some modules from Riaan Booysen:

* wx.lib.flagart:  contains icons of the flags of many countries.

* wx.lib.art.img2pyartprov: makes images embedded in a python file
  with img2py available via the wx.ArtProvider.

* wx.lib.langlistctrl: A wx.ListCtrl for selecting a language,
  which uses the country flag icons.

* An I18N sample for the demo.

wx.lib.masked: Patch from Will Sadkin.  Includes Unicode fixes, plus
more helpful exceptions and ability to designate fields in mask
without intervening fixed characters.

Added wx.SearchCtrl, which is a composite of a wx.TextCtrl with optional
bitmap buttons and a drop-down menu.  Controls like this can typically
be found on a toolbar of applications that support some form of search
functionality.  On the Mac this control is implemented using the
native HISearchField control, on the other platforms a generic control
is used, although that may change in the future as more platforms
introduce native search widgets.

Added a set of button classes to wx.lib.buttons from David Hughes that
uses the native renderer to draw the button.




2.7.2.0
-------
* 7-Nov-2006

Patch [ 1583183 ] Fixes printing/print preview inconsistencies

Add events API to wxHtmlWindow (patch #1504493 by Francesco Montorsi)

Added wxTB_RIGHT style for right-aligned toolbars (Igor Korot)

Added New Zealand NZST and NZDT timezone support to wx.DateTime.

wx.Window.GetAdjustedBestSize is deprecated.  In every conceivable
scenario GetEffectiveMinSize is probably what you want to use instead.

wx.Image: Gained support for TGA image file format.

wx.aui: The classes in the wx.aui module have been renamed to be more
consistent with each other, and make it easier to recognize in the
docs and etc. that they belong together.

======================  =================
FrameManager -->        AuiManager
FrameManagerEvent -->   AuiManagerEvent
PaneInfo -->            AuiPaneInfo
FloatingPane -->        AuiFloatingPane
DockArt -->             AuiDockArt
TabArt -->              AuiTabArt
AuiMultiNotebook -->    AuiNotebook
AuiNotebookEvent -->    AuiNotebookEvent
======================  =================

wx.lib.customtreectrl: A patch from Frank Niessink which adds an
additional style (TR_AUTO_CHECK_PARENT) that (un)checks a parent when
all children are (un)checked.

wx.animate.AnimationCtrl fixed to display inactive bitmap at start
(patch 1590192)

Patch from Dj Gilcrease adding the FNB_HIDE_ON_SINGLE_TAB style flag
for wx.lib.flatnotebook.

wx.Window.GetBestFittingSize has been renamed to GetEffectiveMinSize.
SetBestFittingSize has been renamed to SetInitialSize, since it is
most often used only to set the initial (and minimal) size of a
widget.

The QuickTime backend for wx.media.MediaCtrl on MS Windows works
again.  Just pass szBackend=wx.media.MEDIABACKEND_QUICKTIME to the
constructor to use it instead of the default ActiveMovie backend,
(assuming the quicktime DLLs are available on the system.)






2.7.1.3
-------
* 26-Oct-2006

wxGTK:  The wx.ALWAYS_SHOW_SB style is now supported.

Fixed name errors in the old wxPython package namespace.  As a
reminder, use of this package is deprecated and you are encouraged to
switch your programs over to the wx package.

Fixed wx.glcanvas.GLCanvas.SetCurrent to be compatible with previous
versions.

Added wx.StandardPaths.GetTmpDir.

Bug fixes in the wx.ListCtrl on Mac from Kevin Olivier, allowing it to
send events properly again.  There is also a new native implementation
of wx.ListCtrl available, which will be used for wx.LC_REPORT style
list controls if you set the "mac.listctrl.always_use_generic"
SystemOption to zero.  In a future release this will be the default.

Added a sample to the demo that shows some of what can be done with
the new wx.GraphicsContext and wx.GraphicsPath classes.




2.7.1.2
-------
* 21-Oct-2006

Fixed a bug in the MaskedEdit controls caused by conflicting IsEmpty
methods.

Patch #1579280: Some mimetype optimizations on unix-like systems.

wxMac: Several wx.webkit.WebKitCtrl enhancements/fixes, including:

- new methods for increasing/decreasing text size, getting
  selection, getting/setting scroll position, printing, enabling
  editing, and running JavaScripts on the page.

- added new event (wx.webkit.WebKitBeforeLoadEvent) for catching, and
  possibly vetoing, load events before they occur.

- wx.webkit.WebKitCtrl now fires mouse events for certain events
  that it was eating before. This improves wxSplitterWindow
  resizing behavior.

- refactoring of the sizing logic to move the Cocoa view.  Tested
  with splitter windows, panels, notebooks and all position
  correctly with this.

Some improvements to the drawing code in CustomTreeCtrl.

Fixed refcount leak in wx.Window.GetChildren.





2.7.1.1
-------
* 18-Oct-2006

The following deprecated items have been removed:

* wx.Bitmap SetQuality and GetQuality methods

* The wx.GetNumberFromUser function

* wx.EVT_LIST_GET_INFO and wx.EVT_LIST_SET_INFO

* wx.BookCtrlSizer and wx.NotebookSizer

* The PostScript-specific methods of wx.PrintData

* wx.PrintDialogData SetSetupDialog and GetSetupDialog methods

* wx.FontMapper SetConfig method

* wx.html.HtmlSearchStatus.GetContentsItem method

* wx.html.HtmlHelpData.GetContents, GetContentsCnt, GetIndex, and
  GetIndexCnt methods


wx.EventLoop is now implemented for wxMac.

Added wxPython wrappers for the new wx.Treebook and wx.Toolbook
classes.

wx.DC.BeginDrawing and EndDrawing have been deprecated in the C++
code, so since they never really did anything before they are now just
empty stubs in wxPython.

Solved a problem that has been around for a very long time in how C++
methods are virtualized for overriding in derived Python classes.
Previously we couldn't do it for methods that needed to also exist in
the base class wrappers such that they could be called normally.  (The
reasons are long and complex, but suffice it to say that it was due to
mixing C++'s dynamic dispatch, and Python's runtime lookup of the
method attributes resulting in endless recursion of function calls.)
Because of this problem I used a hack that I have always hated, and
that is renaming the base class methods with a "base_*" prefix, for
example wx.Printout.base_OnBeginDocument.  Now that the problem has
finally been solved I have replaced all the base_Whatever() methods
with the real Whatever() method as well as a simple wrapper named
base_Whatever that is marked as deprecated.  So now instead of writing
your overridden methods like this::

    def OnBeginDocument(self, start, end):
        # do something here
        return self.base_OnBeginDocument(start, end)

You can now call the base class method the normal way, like this::

    def OnBeginDocument(self, start, end):
        # do something here
        return Printout.OnBeginDocument(self, start, end)

Or like this with super()::

    def OnBeginDocument(self, start, end):
        # do something here
        return super(MyPrintout, self).OnBeginDocument(start, end)

Note that the old way with the "base_*" function still works, but you
will get a DeprecationWarning from calling base_OnBeginDocument.  The
classes affected by this are:

* wx.DropSource
* wx.DropTarget
* wx.TextDropTarget
* wx.FileDropTarget
* wx.PyLog   (also added the ability to override Flush)
* wx.PyApp   (also added the ability to override ExitMainLoop)
* wx.Printout
* wx.PyPrintPreview
* wx.PyPreviewFrame
* wx.PreviewControlBar
* wx.Process
* wx.PyControl
* wx.PyPanel
* wx.PyScrolledWindow
* wx.PyWindow
* wx.Timer
* wx.grid.PyGridCellRenderer
* wx.grid.PyGridCellEditor
* wx.grid.PyGridCellAttrProvider
* wx.grid.PyGridTableBase
* wx.html.HtmlWindow
* wx.wizard.PyWizardPage


Added the wx.DC.GradientFillConcentric and wx.DC.GradientFillLinear
methods.

wxGTK: wx.ListBox and wx.CheckListBox are now using native GTK2
widgets.

Added wx.ListBox.HitTest() from patch 1446207

Bumped up to SWIG 1.3.29.  This provides some more runtime performance
boosts, gets rid of the dreaded Ptr classes, and some other nice new
things.

Added wx.Window.GetScreenPosition and GetScreenRect which returns the
position of the window in screen coordinates, even if the window is
not a top-level window.

Added GetResourcesDir and GetLocalizedResourcesDir to
wx.StandardPaths.

Added a GetReceivedFormat method to wx.DataObjectComposite.  You can
use this to find out what format of data object was received from the
source of the clipboard or DnD operation, and then you'll know which
of the component data objects to use to access the data.

Changed how the stock objects (wx.RED, wx.RED_PEN, wx.RED_BRUSH, etc.)
are initialized.  They are now created as uninitialized instances
using __new__.  Then after the wx.App has been created, but before
OnInit is called, the .this attribute of each object is initialized.
This was needed because of some delayed initialization functionality
that was implemented in wxWidgets, but the end result is cleaner for
wxPython as well, and allowed me to remove some ugly code previously
hidden under the covers.

Added wx.StandardPaths.GetDocumentsDir.

Added wx.RendererNative.DrawCheckButton.

wx.ProgressDialog.Update now returns a tuple of two values.  The first
is a continue flag (what was returned before) and the second is a skip
flag.  If the dialog has the wx.PD_CAN_SKIP flag and if the Skip
button is clicked, then the skip flag is set to True the next time
Update is called.

A DeprecationWarning is now issued when the old wxPython package is
imported.  If you are still using the old namespace please convert
your code to use the new wx package instead.

Added wrappers for Julian's new wxRichTextCtrl class, visible in
wxPython as wx.richtext.RichTextCtrl window.  It still needs some more
work, but it is a great start.

wx.lib.mixins.listctrl.TextEditMixin: Fixed the double END_LABEL_EDIT
event problem in TextEditMixin by checking if the editor was already
hidden before continuing with the CloseEditor method.  Also added code
to OpenEditor to send the BEGIN_LABEL_EDIT event and to not allow the
opening of the editor to continue if the event handler doesn't allow
it.

wx.StaticBoxSizer now keeps better track of the wx.StaticBox, and it
will destroy it if the sizer is destroyed before the parent window is.

Added wx.HyperlinkCtrl.

Added battery and power related functions and events (wxMSW only so
far.)  See wx.PowerEvent, wx.GetPowerType and wx.GetBatteryState.

Added wx.ListCtrl.HitTestSubItem which returns the sub-item (i.e. the
column in report mode) that was hit (if any) in addition to the item
and flags.

Added wrappers for wx.ColourPickerCtrl, wx.DirPickerCtrl,
wx.FilePickerCtrl, and wx.FontPickerCtrl.

Patch #1502016 wx.Image.ConvertToGreyscale now retains the alpha
channel.

Added wrappers for the wxAUI classes, in the wx.aui module.

Added the PseudoDC class from Paul Lanier.  It provides a way to
record operations on a DC and then play them back later.

Upgraded to Scintilla 1.70 for wx.stc.StyledTextCtrl.

Added CanSetTransparent and SetTransparent methods to the
wx.TopLevelWindow class, with implementations (so far) for wxMSW and
wxMac.

SetDefaultItem() and GetDefaultItem() are now members of
wx.TopLevelWindow, not wx.Panel.

wxGTK: Stock items (icons) will be used for menu items with stock
IDs.

Added wx.lib.combotreebox from Frank Niessink

Added wx.ImageFromBuffer, wx.BitmapFromBuffer and
wx.BitmapFromBufferRGBA factory functions.  They enable loading of an
image or bitmap directly from a Python object that implements the
buffer interface, such as strings, arrays, etc.

Added wx.App.IsDisplayAvailable() which can be used to determine if a
GUI can be created in the current environment.  (Still need an
implementation for wxMSW...)

The wx.html.HTML_FONT_SIZE_x constants are no longer available as the
default sizes are now calculated at runtime based on the size of the
normal GUI font.

wx.Colour now includes an alpha component, which defaults to
wx.ALPHA_OPAQUE.  This is in preparation for allowing various new
alpha blening functionality using wx.Colour objects, such as drawing
with pens and brushes on a wx.DC.

Added wx.NativePixelBuffer, wx.AlphPixelBuffer and related iterator
and accessor classes.  They allow platform independent direct access
to the platform specific pixel buffer inside of a wx.Bitmap object.

The beginnings of support for RTL languages has been added, thanks to
a Google SoC project.

Added wx.lib.dragscroller from Riaan Booysen.  It provides a helper
class that can used to scroll a wx.ScrolledWindow in response to a
mouse drag.

Applied patch 1551409: Adds support for indeterminate mode gauges.

wxMac: I've turned on the compile option for using the native toolbar
on the Mac now that it supports hosting of controls.  If the toolbar
is managed by the frame via either CreateToolBar() or SetToolBar()
then the native toolbar will be used.  Additional toolbars, or
toolbars that are not children of the frame, are managed by sizers or
what-not will still use the emulated toolbar because of platform
restrictions in how/where the native toolbar can be used.

Added Python properties for many of the getter/setter methods of wx
classes.  In order for the names to be predictable for somebody
already familiar with wxPython the property names are simply the name
of the getter with the "Get" dropped.  For example, wx.Window has a
property named "Size" that maps to GetSize and SetSize.  So far there
is only one known name conflict using this naming convention, and that
is wx.KeyEvent.KeyCode, however since KeyCode was formerly a
compatibility alias for GetKeyCode (and has been for a long time) it
was decided to just switch it to a property.  If you want to use the
method then change your calls to event.KeyCode() to
event.GetKeyCode(), otherwise you can use it as a property just by
dropping the parentheses.

Updated the C++ code for wx.gizmos.TreeListCtrl from the wxCode
project.  This has resulted in some minor API changes, most of which
were worked around in the wrapper code.

Added wx.lib.delayedresult from Oliver Schoenborn.

Added wx.lib.expando, a multi-line textctrl that expands as more lines
are needed.

wx.Image.Scale and Rescale methods now take an extra parameter
specifying type of method to use for resampling the image.  It
defaults to the current behavior of just replicating pixels, if
wx.IMAGE_QUALITY_HIGH is passed then it uses bicubic and box averaging
resampling methods for upsampling and downsampling respectively.

Added the wx.lib.buttonpanel module, which is a tweaked version of
Andrea Gavana's FancyButtonPanel module.

Added the wx.lib.flatnotebook module, from Andrea Gavana.

Renamed wx.FutureCall to wx.CallLater so it is named more like
wx.CallAfter.  wx.FutureCall is now an empty subclass of wx.CallLater
for compatibility of older code.

Added the wx.lib.customtreectrl module from Andrea Gavana.

Added ChangeSelection to wx.BookCtrl (the base class for wx.Notebook
and other book controls) that is the same as SetSelection but doesn't
send the change events.

Added wx.TextCtrl.ChangeValue() which is the same as SetValue() but
doesn't send the text changed event.

For consistency, all classes having an Ok() method now also have
IsOk(), use of the latter form is preferred although the former hasn't
been deprecated yet

Added the wx.AboutBox() function and wx.AboutDialogInfo class.  They
provide a way to show a standard About box for the application, which
will either be a native dialog or a generic one depending on what info
is provided and if it can all be shown with the native dialog.

The code in the animate contrib has been moved into the core wxWidgets
library, and refactored a bit along the way.  For wxPython it still
exists in the wx.animate module, but has basically been reduced to two
classes, wx.animate.Animation, and wx.animate.AnimationCtrl.  You load
the animated GIF (and hopefully there will be other supported formats
in the near future) in the Animation object, and then give that to the
AnimatedCtrl for display.  See the demo for an example.  There is also
still a GIFAnimationCtrl class that provides some level of backwards
compatibility with the old implementation.

wxMac: The compile option that turns on the use of CoreGraphics (a.k.a
Quartz) for wxDC is now turned on by default.  This means that all
drawing via wxDC is done using the new APIs from apple, instead of the
old Quick Draw API.  There are, however, a few places where Quartz and
wxDC don't fit together very well, mainly the lack of support for
logical drawing operations such as XOR, but there is work in progress
to provide other ways to do the same sort of thing that will work with
Quartz and also on the other platforms.

The first parts of a new 2D drawing API has been added with the
wx.GraphicsPath and wx.GraphicsContext classes.  They wrap GDI+ on
Windows, Cairo on wxGTK and CoreGraphics on OS X.  They allow path-based
drawing with alpha-blending and anti-aliasing, and use a floating
point coordinate system.  Currently they can only target drawing to
windows, but other wx.DC backends are forthcoming.  The APIs may
evolve a bit more before they are finalaized with the 2.8 release, but
there is enough there now to get a good feel for how things will work.
There is also a transitional wx.GCDC class that provides the wx.DC API
on top of wx.GraphicsContext.  Docs and a demo are still MIA.

Added a wx.AutoBufferedPaintDC that is a subclass of wx.PaintDC on
platforms that do double buffering by default, and a subclass of
wx.BufferedPaintDC on the platforms that don't.  You can use this
class to help avoid the overhead of buffering when it is not
needed. There is also a wx.AutoBufferedPaintDCFactory function that
does a little more and actually tests if the window has
double-buffering enabled and then decides whether to return a
wx.PaintDC or wx.BufferedPaintDC.  This uses the new
wx.Window.IsDoubleBuffered method.







2.6.3.3
-------
* 15-July-2006

wx.lib.pubsub updates from Oliver Schoenborn:
    - fixed the hash problem with non-hashable objects
    - now supports listeners that use \*args as an argument
      (listener(\*args) was not passing the validity test)
    - corrected some mistakes in documentation
    - added some clarifications (hopefully useful for first time
      users)
    - changed the way singleton is implemented since old way prevented
      pydoc etc from extracting docs for Publisher

DocView and ActiveGrid IDE updates from Morgan Hua:
    New Features: In Tab-View mode, Ctrl-number will take the user to
    the numbered tab view.  Modified files now show an '*' astrisk in
    the view title.  Debugger framework can now support PHP debugging.
    Not important for python development, but at least that means the
    debugger framework is more generalized.

wx.lib.mixins.listctrl.TextEditMixin: Fixed the double END_LABEL_EDIT
event problem in TextEditMixin by checking if the editor was already
hidden before continuing with the CloseEditor method.  Also added code
to OpenEditor to send the BEGIN_LABEL_EDIT event and to not allow the
opening of the editor to continue if the event handler doesn't allow
it.

Undeprecated wx.GetNumberFromUser and added wx.NumberEntryDialog.

Made necessaary changes for building wxPython for Python 2.5.  There
may still be some issues related to the new Py_ssize_t type and 64-bit
machines, but at least all compile errors and warnings related to it
have been resolved.




2.6.3.2
-------
* 3-April-2006

Fixed reference leak in wx.gizmos.TreeListCtrl.GetSelections.

wxMSW: Fixed sizing issue with wx.Choice and wx.ComboBox.  This change
was implemented by reverting a prior fix for a different problem
(contiuous painting/resizing when a combobox is used as a widget in a
wx.html.HtmlWindow) so a method to fix both problems is still being
investigated.

wxGTK: Fixed potential buffer overrun when pasting from the
clipboard.

Fixed problem in wx.lib.splitter when used on 64-bit platforms.  Used
the current length of the list for specifying an append instead of
sys.maxint.

wxMSW: Support added for XP themed owner drawn buttons and bitmap
buttons.  For example, if you change the foreground color of a button
it will now be drawn with the XP themed style rather than an ugly
generic button style.

XRCed: Fix for Copy/Paste objects with international characters.

Fixed the equality and inequality operators for some of the basic
data types (wx.Point, wx.Size, wx.Colour, etc.) to no longer raise a
TypeError if the compared object is not compatible, but to just return
a boolean as expected.  For example::

          wx.Colour(64,0,64) == 123      ==> False

wxMSW: Fixed (again) sizing/positioning issues of calling Realize on
a wx.ToolBar that is not manaaged directly by a frame and that is
already shown.

wxMSW: Fixed wx.Choice/wx.ComboBox so they send events when a new item
is selected only with the keyboard.



2.6.3.0
-------
* 27-March-2006

Change the wx.ListCtrl InsertStringItem wrapper to use the form that
takes an imageIndex, and set the default to -1.  This ensures that on
wxMSW that if there is an image list but they don't specify an image,
the native control doesn't use one anyway.

wxMSW: wx.ListCtrl in report mode is now able to support images in
other columns besides the first one.  Simply pass an image index to
SetStringItem.  For virtual list controls you can specify the image to
use on the extra columns by overriding OnGetItemColumnImage in your
derived class.  It is passed the item number and the column number as
parameters, and the default version simply calls OnGetItemImage for
column zero, or returns -1 for other columns.

Switched to using SWIG 1.3.27 for generating the wrapper code.  There
are some small changes needed to SWIG to work around some bugs that
wxPython exposes, and to be able to generate code that matches that
which wxPython is using.  If you are building wxPython yourself and
need to modify any of the \*.i files or to add your own, then you will
want to be sure to use a matching SWIG.  See wxPython/SWIG/README.txt
in the source tarball for details.

wx.Image.Copy, Mirror, and GetSubImage now also do the right thing
with  the alpha channel.

wxMSW: Fixed problem in wx.TextCtrl where using SetValue and
wx.TE_RICH2 would cause the control to be shown if it was hidden.

wxMSW: Numpad special keys are now distinguished from normal keys in
key events.

wxMSW: Multiline notebook tab label change now resizes the control
correctly if an extra row is removed or added.

wxMSW: On XP fall back to unthemed wxNotebook if specified orientation
not available in the themed version.

Added wx.Toolbar.GetToolsCount.

Added wx.GridSizer.CalcRowsCols.

Added wx.OutputStream.LastWrite.

wxGTK: EVT_SET_CURSOR is now sent.

wxGTK: Fix RequestMore for idle events.

wxGTK: Implement user dashes for PS and GNOME printing.

wxGTK: Correct update region code. Don't always invalidate the whole
window upon resize. Re-enable support for thewx.NO_FULL_REPAINT_ON_RESIZE
flag.  Also disable refreshing custom controls when focusing in and out.

wx.lib.pubsub: Publisher is now able to parse a dotted notation string
into a topic tuple.  For example: subscribing to "timer.clock.seconds"
is the same as subscribing to ("timer", "clock", "seconds").

Applied patch #1441370: lib.plot - allow passing in wx.Colour()

Added wx.CommandEvent.GetClientData.

Updated wxStyledTextCtrl to use version 1.67 of Scintilla.
NOTE: The STC_LEX_ASP and STC_LEX_PHP lexers have been deprecated,
you should use STC_LEX_HTML instead.

wxSTC: Implemented Fix for SF Bug #1436503.  Delay the start of the
DnD operation in case the user just intended to click, not drag.

Updated the analogclock.py module to the new analogclock package from
E. A. Tacao.

Added the wx.lib.mixins.listctrl.CheckListCtrlMixin class from Bruce
Who, which makes it easy to put checkboxes on list control items.

Applied a patch from Christian Kristukat to wx.lib.plot that adds
scrollbars when the plot is zoomed in, and also the ability to grab a
zoomed plot and move it around with a mouse drag.

XRCed updated to allow wxMenuBar to be created inside a wxFrame.

Added wx.StandardPaths.GetDocumentsDir() (patch 1214360)






2.6.2.1
-------
* 10-Jan-2006

wxMSW: Fix for bug #1211907, popup menu indenting inconsistent with
bitmaps.

wxMac: Don't send an event for wx.RadioButton deselections, just the
selections.  This was done to make it consistent with the other
platforms.

wxMSW: Always set flat toolbar style, even under XP with themes: this
is necessary or separators aren't shown at all.

Fixes for bug #1217872, pydocview.DocService not correctly initialized.

Fix for bug #1217874, Error in parameter name in DocManager.CreateView.

Added wrappers for the wx.RendererNative class.

Added the wx.lib.splitter module, which contains the
MultiSplitterWindow class.  This class is much like the standard
wx.SplitterWindow class, except it allows more than one split, so it
can manage more than two child windows.

Docview and IDE patch from Morgan Hua with fix for bug #1217890
"Closing view crashes Python" plus some new features:

    New feature added to the IDE is 'Extensions'.  Under
    Tools|Options|Extensions, you can add calls to external programs.
    For example you can add a "Notepad" extension (under windows) that
    will exec Notepad on the currently open file.  A new "Notepad"
    menu item will appear under the Tools menu.

Some fixes to XRCed to make encoding errors a bit more user friendly.

XRCed changes from Roman Rolinsky:

* Added new controls (Choicebook, Listbook, StatusBar,
  DatePicker), and completed style flags. Test window is opened
  for an available parent control if no specific view
  defined. Better handling of exceptions (highlighting does not
  'stick' anymore).

* Use system clipboard for Copy/Paste.

* Improved some dialogs (window styles, growable cols). Changed
  the range for wxSpinCtrl min/max to all integers (default 0/100
  is not always good).

Updates for wx.lib.foldpanelbar and wx.lib.hyperlink from Andrea
Gavana.

Fix for Bug #1283496: wxPython TheClipboard class causes problems for
pychecker.  Ensure the app has been created before initializing
wx.TheClipboard.

Fix for Bug #1352602: FileBrowseButtonWithHistory can't type in Value.

wxHTML: Added space after list item number.

wx.lib.printout:  Applied patch #1384440.

wxMSW:  Fix for Bug #1293225 Window_FromHWND crashes if parent is
None.

Fix for Bug #1261669, use a wx.TE_RICH2 style for the Process demo so
it doesn't fill up too soon.

Applied Patch #1354389: wxPython MenuItem SetBitmaps fix.

Applied Patch #1239456: wxPython wx.DataObject.GetAllFormats fix.

Applied Patch # #1230107 which allows image handlers to be written in
Python by deriving from wx.PyImageHandler.

Applied patch #1072210: generalize printout.py to allow text printing.

Applied patch #1243907: Give Throbber much more flexibility by
allowing the user to set the rest image, the direction, the current
index, custom sequence.  Allows user to manually step through the
sequence with Next(), Previous(), Increment(), Decrement() &
SetCurrent(). Very handy if you have multiple throbbers that you want
to synchronize with a single timer.

Fix for bug #1336711: wx.lib.calendar.CalenDlg can yield incorrect
result.

Applied patch from Morgan Hua for updates to ActiveGrid code
(pydocview, ActiveGrid IDE, etc.)

Applied patch #1326241: Supporting "setup.py install --install-headers=path"

Applied patch from Morgan Hua to fix bug #1219423: CommandManager
should not repeat old commands after a branch.

Applied patch #1238825 adding search backward capabilities to the
demo.  Modified to use the up/down options in the wx.FindReplaceDialog
instead of a separate menu item.

Fix for bug #1266745 and #1387725 in the wx.FindReplaceDialog on MSW.
Actually check we are using MSLU before doing the hack designed to
workaround a bug in MSLU!

wxMSW: wx.lib.iewin.IEHtmlWindow now properly handles tabbing, return
and other special keys properly.

Lots of PyCrust enhancements started by Franz Steinaeusler, Adi Sieker,
and Sebastian Haase, and which in turn were further enhanced, fixed
tweaked and finished up by me.  The changes include the following:

* The Autocomplete and Calltip windows can now be opened manually
  with Ctrl-Space and Ctrl-Shift-Space.

* In the stand alone PyCrust app the various option settings,
  window size and position, and etc. are saved and restored at the
  next run.

* Added a help dialog bound to the F1 key that shows the key
  bindings.

* Added a new text completion function that suggests words from
  the history.  Bound to Shift-Return.

* F11 will toggle the maximized state of the frame.

* switched to Bind() from wx.EVT_*().

* Display of line numbers can be toggled.

* F12 toggles a "free edit" mode of the shell buffer.  This mode
  is useful, for example, if you would like to remove some output
  or errors or etc. from the buffer before doing a copy/paste.
  The free edit mode is designated by the use of a red,
  non-flashing caret.

* Ctrl-Shift-F will fold/unfold (hide/show) the selected lines.

* General code cleanup and fixes.

* Use wx.StandardPaths to determine the location of the config
  files.

* Use wx.SP_LIVE_UPDATE on crust and filling windows.

* Extended the saving of the config info and other new features to
  the PyShell app too.  Additionally, other apps that embed a
  PyCrust or a PyShell can pass their own wx.Config object and
  have the Py code save/restore its settings to/from there.

* All of the classes with config info get an opportunity to
  save/load their own settings instead of putting all the
  save/load code in one place that then has to reach all over the
  place to do anything.

* Enable editing of the startup python code, which will either be
  the file pointed to by PYTHONSTARTUP or a file in the config dir
  if PYTHONSTARTUP is not set in the environment.

* Added an option to skip the running of the startup code when
  PyShell or PyCrust starts.

* PyCrust adds a pp(item) function to the shell's namespace that
  pretty prints the item in the Display tab of the notebook.
  Added code to raise that tab when pp() is called.

* Added an option for whether to insert text for function
  parameters when popping up the call tip.

* Added Find and Find-Next functions that use the
  wx.FindReplaceDialog.


Applied patches from Will Sadkin for wx.lib.masked modules:

* Now ignores kill focus events when being destroyed.

* Added missing call to set insertion point on changing fields.

* Modified SetKeyHandler() to accept None as means of removing
  one.

* Fixed keyhandler processing for group and decimal character
  changes.

* Fixed a problem that prevented input into the integer digit of a
  integerwidth=1 numctrl, if the current value was 0.

* Fixed logic involving processing of "_signOk" flag, to remove
  default sign key handlers if false, so that
  SetAllowNegative(False) in the NumCtrl works properly.

* Fixed selection logic for numeric controls so that if
  selectOnFieldEntry is true, and the integer portion of an
  integer format control is selected and the sign position is
  selected, the sign keys will always result in a negative value,
  rather than toggling the previous sign.

wx.FontMapper.SetConfig is deprecated.  You should instead just set an
application-wide config object with wx.Config.Set, which wx.FontMapper
will use by default.

Added wx.GetMouseState which returns the current state of the mouse.
It returns an instance of a wx.MouseState object that contains the
current position of the mouse pointer in screen coordinants, as well
as boolean values indicating the up/down status of the mouse buttons
and the modifier keys.

Added wx.SizerItem.SetUserData

A variety of updates to wx.lib.floatcanvas, including Added
DrawObjects, including a ScaledTextBox, with auto-wrapping, etc, and
Scaled and Unscaled Bitmap Objects.

.. warning:: Changed all DrawObjects to take an (x,y) pair rather
       than individual x,y parameters. Also changed rectangles and
       ellipses to take (w,h) pair. This is an API change, but should
       be easy to accommodate, all you need to do is add a parenthesis
       pair:  (...x, y, ...) --->  (...(x,y), ...)




2.6.1.0
-------
* 4-June-2005

wx.ListCtrl: patch #1210352, fixes editing in generic wx.ListCtrl with
wx.LC_EDIT_LABELS.

Applied patch #208286, MediaCtrl DirectShow rewrite.

DocView patches from Morgan Hua: bug fixes, and additional SVN
commands, also added a default template that uses the text editor for
any unknown file type.

wxMSW: Use the system IDC_HAND cursor for wx.CURSOR_HAND and only fallback
to the strange wxWidgets version if the system one is not available.

wx.grid.Grid: Merge the cell size attribute the same way that other
attributes are merged, e.g., if it is already set to a non-default
value in the current GridCellAttr object then don't merge from the
other.

wx.lib.evtmgr: Fixed to use wx._core._wxPyDeadObject

wx.lib.gridmovers: Don't scroll when the mouse is dragged outside of
the grid, unless the mouse is kept in motion.

wxMSW:  Applied patch #1213290 incorrect logic in
wx.TopLevelWindow.ShowFullScreen.

Applied patch #1213066 correct device names for Joystick in Linux.

wxGTK: Applied patch #1207162 wx.TextCtrl.SetStyle fix for overlapping
calls.

wx.FileConfig: fixed DeleteEntry to set the dirty flag properly so the
change will get written at the next flush.





2.6.0.1
-------
* 30-May-2005

Added wx.BrushFromBitmap to create a stippled brush in a single step.
Also added missing brysh style flags: wx.STIPPLE_MASK
wx.STIPPLE_MASK_OPAQUE.

wxMSW: Fix for default control colours when the system text fg colour
is not black.

wxGTK: Patch #1171754, It is now possible to have a menu item that
both has an icon and is a submenu.

wxMSW: Patch #1197009, better refreshes when windows are moved and
resized.

wxMSW: Patch #1197468.  Keeps track of pending size/position changes
in case there is more than one adjustment for a window in a single
DeferWindowPos set, then the pending values can be used for defaults
instead of current values.

Fixed the typemap that converts a Python list of strings to a
wxArrayString so it uses the wxPython default encoding.

Several docstrings added and updated.  Lots more to go.

wxMac: Strings added to the clipboard or used in DnD no longer have an
extra null character at the end.

Added wx.GetXDisplay that returns a raw swigified pointer for the X11
Display, or None for the non-X11 platforms.

wxMenu: Don't send an event when selecting an already selected radio
item.

Added wx.LaunchDefaultBrowser.

wxMSW: Fixed erroneous selection of content in wx.ComboBox when within
a wx.StaticBox.

wxMSW: Fixed alpha blitting to take into account source position.

Ensure that Python is still in an initialized state before doing any
locking or unlocking in wxPyBeginBlockThreads and wxPyEndBlockThreads
as these can be triggered after Python has been finalized in embedding
situations.

Added alternate constructors for wx.Font: wx.FontFromPixelSize,
wx.FFont, wx.FFontFromPixelSize.  See the docstrings or new api docs
for details.

Added wx.lib.hyperlink from Andrea Gavana.  It is a control like
static text that acts like a hyper-link, launching the system's
default browser in response to the clicks.

Added an optional parameter to wxversion.select that allows you to
specify that the extra components specified in the version string are
required.  For example, if you ask for "2.6-unicode" but only the ansi
version is installed then by default the ansi version will be selected
as it considered close enough since the version numbers match.  If you
want to force the options to be required then you can just add a True
parameter, like this::

         import wxversion
         wxversion.select("2.6-unicode", True)
         import wx

Tweaked wx.lib.buttons such that flat buttons (e.g. have no bevel and
a wx.BORDER_NONE style flag) paint themed backgrounds if there are
transparent areas and the parent is displaying a theme.

wxMSW:  Fix for wrong sash colour of wx.SplitterWindow in the silver
theme on XP.

Added a wx.xrc.XmlResourceHandler for the Ticker class.  See
wx/lib/ticker_xrc.py

wxSTC: Fixed CmdKeyAssign key bindings for Ctrl-Backspace.

wxMSW: Fixed a bug in wx.TextCtrl where all the lines were being used
to calculate the best size, instead of using a reasonable limit.

XRCed: Use wx.GetDefaultPyEncoding/wx.SetDefaultPyEncoding for
changing active encoding.  Fixed pasting siblings (Ctrl key pressed
while pasting).

wx.lib.filebrowsebutton: Bug fix from Chad Netzer for when
self.history is None.

wx.ogl: Patch from Davide Salomoni that adds an optional point
parameter to LineShape.InsertLineControlPoint allowing one to
optionally specify where the new control point has to be drawn.

wxMSW: setting foreground colour for wx.CheckBox now works when using
XP themes.

More updates to the docview library modules and sample apps from the
ActiveGrid folks.  Their sample IDE is now able to integrate with
Subversion.

wx.grid.Grid:  Ensure that the grid gets the focus when it is
left-clicked.  Note that if you have custom widgets that handle the
EVT_LEFT_DOWN event but do not call event.Skip() then you will
probably want to add a call to self.SetFocus in the event handler.

wxGTK:  Add wxSTAY_ON_TOP support [Patch 1206023]

wx.TreeCtrl:  wx.EVT_TREE_ITEM_MENU event made consistent on all
platforms.  The location of the click or the item is included in the
event as well.

wxGTK: Setting background colour of a window now only affects the
window itself, not the borders, scrollbars, etc.  (Bug #1204069)

Print framework:  Add more paper sizes and code to fallback to an
explicit paper size if a known paper size is not found for the
printer.

wxMac: Applied patch for bug #1206181 Option-key decodes are wrong,
also applied patch for bug #1205691 Modified Fn keys don't work.

wx.Image: Fixed to preserve alpha channel in Rotate90 method.

wxMSW: Fixed incorrect background colour on wx.CheckListBox.

wxMSW: Fixed drawing of owner drawn buttons with multiline labels

Removed a bunch of unnecessary files, and removed or replaced images
that we're not sure of their origin or license.

The default DoGetBestSize is updated to not always return the current
size if the window has no sizer, children, or minsize set.  Instead
the current size is set as the minsize.  This solves the occasional
problem where a sizer may cause a childless panel to grow but never
shrink.

wxMSW: When converting a wx.Icon to a bitmap check if the icon has an
alpha channel and set the bitmap to use it.

Fixed the wrong class name used in wx.PyScrolledWindow's call to
_setCallbackInfo.

wxMSW: patch #1207202, Fixes GDI leak when using stock cursors.

wx.calendar.CalendarCtrl: Patch #1207531, Keeps the CalendarCtrl wide
enough even when the weekday names for the locale are shorter than
usual.

Made GridCellNumberEditor.StartingKey also insert the typed char when
there is a range of allowed values (so a wx.SpinCtrl is used instead
of a wx.TextCtrl.)





2.6.0.0
-------
* 26-Apr-2005

wxMSW: Fixed wx.TransientPopupWindow (and therefore wx.TipWindow) to
auto-dismiss when the mouse is clicked outside of the popup like it is
supposed to.

wxMSW: Fixed bug #1167891 wx.Notebook display problem with wx.NB_MULTILINE.

wxMSW: Fixed bad cliping of hidden windows inside of wx.StaticBox.

wxGTK:  The configure flags for selecting GTK+ 1.2.x or 2.x has
changed slightly.  It is now --with-gtk[=VERSION] where VERSION is
either '1', '2' or 'any'.  The default is '2'.

wx.stc.StyledTextCtrl: Added the following methods for alternate ways
to set and fetch text from the document buffer.  They work similarly
to the existing methods of the same name, except that they don't go
through the same string/unicode <--> wxString conversions.  The "Raw"
methods will do no conversions at all and in a unicode build of
wxPython the strings will be in the utf-8 encoding and in an ansi
build no assumption is made about the encoding.  The "UTF8" functions
will attempt to always get/set utf-8 text, which it will always be
able to do in a unicode build, and in an ansi build it will depend on
the content of the utf-8 used being compatible with the current
encoding, (you'll get an exception otherwise.)

===================  ====================
AddTextRaw           AddTextUTF8
InsertTextRaw        InsertTextUTF8
GetCurLineRaw        GetCurLineUTF8
GetLineRaw           GetLineUTF8
GetSelectedTextRaw   GetSelectedTextUTF8
GetTextRangeRaw      GetTextRangeUTF8
SetTextRaw           SetTextUTF8
GetTextRaw           GetTextUTF8
AppendTextRaw        AppendTextUTF8
===================  ====================


wx.stc.StyledTextCtrl:  Added the StyleSetFontEncoding(style, enc)
method that allows you to set the encoding to be used by the font for
a particular style.

wxMac: Fixed wx.ComboBox to forward the EVT_CHAR, EVT_KEY_DOWN,
EVT_KEY_UP and EVT_TEXT events from its embedded text control.

wxMac: Corrected refresh bugs in wxGrid.

XRCed: Updated to version 0.1.5.
    * Added wxWizard, wxWizardPageSimple (only from pull-down menu).
    * Hide command for test window.
    * Replacing classes works better.
    * Added Locate tool.




2.5.5.1
-------
* 8-Apr-2005

wxMSW: Fixed bug #1022383, 'several ComboBoxes appear selected'

wx.grid.Grid: Fixed bug #1163384.  Moved the code that handles
activating the cell editors to a EVT_CHAR event handler.  This is done
so the character inserted into the editor will be the "cooked" char
value (including accented or composed keys) rather than the raw code
provided by the EVT_KEY_DOWN event.

Added orient parameter to wx.MDIParentFrame.Tile()

wxMSW: wxTextCtrl with wx.TE_RICH2 style now uses RichEdit 4.1 if
available.

Added GetCount, GetCountRGB, and GetCountColour methods to
wx.ImageHistogram.

wxMSW: wx.Window.Refresh changed to explicitly refresh all children as
well as the parent.  Previously it was implicitly done because parents
did not clip their children by default.  Now that they always clip
children then Refresh needed to be fixed to do a recursive refresh.
This also fixes the Freeze/Thaw problems that some people had with
2.5.4.1.

wx.SplitterWindow: Send EVT_SPLITTER_SASH_POS_CHANGED only once after
end of dragging and not after each CHANGING event (modified patch
#1076226)

wx.glcanvas.GLCanvas: applied patch fixing problems with X server
crash when using nVidia cards (patch 1155132)

wx.lib.mixins.listctrl: Patches from Toni Brkic:
   * Bugfix for TextEditMixin when the view can't be scrolled
   * Enhancement for ListCtrlAutoWidthMixin, allowing it to manage
     the width of any column.

wxMac: removal and reusing toolbar tools like the other platforms is
now possible.

wxMac: Correct radio tool selection after calling Realize a 2nd time.

wxMSW: Applied patch #1166587, removes all flicker from wx.StaticBox

Added wx.lib.foldpanelbar, Andrea Gavana's port of Jorgen Bodde's C++
wxFoldPanelBar classes to Python.

wxGTK: Applied patch #1173802, reimplementation of GtkFileChooser
wxFileDialog by Mart Raudsepp.  Note that this new file dialog is only
used on GTK2 >= 2.4.  For earlier GTK2 versions and GTK1 then the
older generic file dialog is used.

wxMSW: fixes to static box borders calculations (finalizes patch
#1166587)

wx.Image: Use Python's buffer interface API for all image data and
alpha Set/Get methods and the ImageFromData* constructors.  They all
still copy the buffer except for SetDataBuffer and SetAlphaBuffer, but
this gives more flexibility on where the data can come from.

Added MDI support to XRC

Added wx.animate module and a demo.  The wx.animate module provides a
control that is able to display an animated GIF file.

wx.lib.plot.py: Applied patch from Werner F. Bruhin that allows either
vertical and/or horizontal gridlines.

wxMSW: Extra space given for top border of wx.StaticBoxSizer so the
upper line is not cliped when there is no label.

wxMSW: Restored old behaviour of wx.StaticBox.SetBackgroundColour only
affecting the label.

wxMSW: Fixed missing EVT_RIGHT_DOWN and EVT_TREE_ITEM_RIGHT_CLICK
events in a wx.TreeCtrl.

Added wx.GetTopLevelWindows() function which returns a copy of the
list of top-level windows that currently exist in the application.

Updated docview library modules and sample apps from the ActiveGrid
folks.

Added the ActiveGrid IDE as a sample application.




2.5.4.1
-------
* 16-Mar-2005

wx.Sizer Add, Insert, and Prepend functions now return a reference to the
wx.SizerItem that was added to the sizer, and the wx.SizerItem has a
GetRect accessor to give the position of the item on the parent window.

Added wx.Sizer.GetItem method which returns the wx.SizerItem for the given
wx.Window, wx.Sizer or position index.

wxMSW: wx.RadioButtons in the same group no longer have to be
consecutive (there may be intervening controls). Without this fix, an
out-of-sync assert is generated when clicking on a radio button and
then calling GetValue().

Some XRC changes:
    - Added 'icon' property to wxFrame and wxDialog
    - No longer ignores menu bitmaps on non-MSW platforms
    - Notebook page bitmaps are now supported
    - added system colours and fonts support (based on patch #1038207)

wxMSW: fix for [ 1052989 ] TextCtrl.SetBackgroundColour(wx.NullColour)
bug.

Added wx.PasswordEntryDialog analogous to wx.TextEntryDialog, allows
detecting entering an empty string vs. cancel unlike the
wx.GetPasswordFromUser dialog function.

OGL patch from Shane Holloway:

    Two simple problems found in the new python ogl code.  First is
    the patch for _canvas.py.  Essentially::

        dx = abs(dc.LogicalToDeviceX(x - self._firstDragX))
        dy = abs(dc.LogicalToDeviceY(y - self._firstDragY))

    was incorrect because (x,y) and (self._firstDragX,
    self._firstDragY) are both already in Logical coordinates.
    Therefore the difference between the two is also in logical
    coordinates, and the conversion call is an error.  This bug
    surfaces when you have OGL on a scrollwin, and you are far from
    the origin of the canvas.

    The second change in _composit.py basically removes the assumption
    that the child is in both self._children and self._divisions.
    Causes many problems when it's not.  ;)

Fixed GetSaveData and SetSaveData in wx.lib.multisash to not depend on
the default way that class objects are converted to strings.

Fixed problem in StyledTextCtrl.Set[HV]ScrollBar that could leave the
internal scrollbar visible.

Added wx.StandardPaths which provides methods for determining standard
system paths for each platform.

wxMSW: The window background is now only erased by default if the
background colour or background mode has been changed.  This better
allows the default system themed behaviour to show through for
uncustomized windows.  Explicit support added for using the correct
theme texture for wx.Notebook pages and their children.

wx.Image: Added support for alpha channels in interpolated and
non-interpolated image rotation.  Added ConvertAlphaToMask helper
method for turning shades of grey into shades of alpha and a colour.

wxGTK2: Reimplemented DoDrawRotatedText() by way of a rotation of an
alpha blended text bitmap.  It would be better if Pango could draw
directly into an wxImage (as FreeType can,) but that is for later...

Added wrappers and a demo for the wx.MediaCtrl class, which can play
various forms of audio/video media using native codecs install on the
system.  So far it is only implemented for Windows and OSX.

wxGTK: Patch applied for Freeze()/Thaw() for wxTextCtrtl.

Added "gravity" for splitter window (patch 1046105). Gravity is a
floating-point factor between 0.0 and 1.0 which controls position of
sash while resizing the wx.SplitterWindow.  The gravity specifies
how much the left/top window will grow while resizing.

wxMSW: wx.Slider's C++ implementation rewritten to be more
maintainable and hopefully less buggy.  The position of the labels has
also been changed in order to better comply with Microsoft's examples
of how to use the control.

wxMSW:  Fix wx.TreeCtrl to end label editing if the control loses
focus (a slightly modified patch 1084592.)

Added wx.EXEC_NODISABLE flag for wx.Execute, which will prevent all
the app's windows being disabled while a synchronous child process is
running.

wxMSW: Much work to correct painting (or leaving transparent) of
control backgrounds, properly using background themes on XP, etc.

Fixed a circular reference problem with wx.Timer.  It will now
completely cleanup after itself when the last reference to the timer
is removed.  If you were previously using timer.Destroy() to cleanup
your timers it will no longer work.  Instead you should hold a
reference to the timer and then del the reference when you are
finished with the timer.

Updated to 1.3.24 of SWIG.  All of my big patches have been applied to
the main SWIG source tree, but unfortunately there were also some bugs
added that affected the wxPython build and a few details in my
original patch were changed/removed, so we are still not free of
patches.  A new patch for SWIG is located in the wxPython/SWIG
directory of the wxPython source tree.  SWIG 1.3.24 plus this patch
should be used by anyone who is making custom modifications to
wxPython's .i files, or building their own extension modules or
etc. that need to interact with the wxPython swigged types.  For the
morbidly curious, here are a few more details:

* Since it is now possible easily and simply share the SWIG type
  tables across modules I reverted to always using the stock SWIG
  runtime instead of my slightly hacked up version of it exported
  via the wxPython C API.

* The %name directive is now deprecated so I replaced most uses of
  it with a custom %Rename macro that uses %rename internally.
  These will evetually need to be replaced with a DocDecl macro
  when docstrings are added for those items.

* The "this" attribute of all SWIGged classes is no longer a
  string containing a "swigified pointer", but rather a custom
  built-in type that holds the real C pointer to the object and
  the type info.  It can be converted to a string like the old
  value using str() or to the long integer value of the pointer
  using long().

Added SetDefaultPyEncoding and GetDefaultPyEncoding functions which
will set/get the encoding used by wxPython to convert string or
unicode objects to/from wxString objects.  Previously the default
Python encoding was always used, but unless the user had tweaked their
sitecustomize.py file it is always "ascii", which would result in
errors if the strings contained character codes >= 128.
SetDefaultPyEncoding will now allow you to control which encoding will
be used to do those conversions.  The default encoding is set to the
value of `locale.getdefaultlocale()[1]` when wxPython is first
imported.  Please see http://www.alanwood.net/demos/charsetdiffs.html
for information on the differences between the common latin/roman
encodings.

Added wxStdDialogButtonSizer, which is a a special sizer that knows
how to order and position standard buttons in order to conform to the
current platform's standards.  You simply need to add each `wx.Button`
to the sizer, and be sure to create the buttons using the standard
ID's.  Then call `Realize` and the sizer will take care of the rest.

wxMSW Toolbar: pass correct tool id (and not always -1) to the
EVT_TOOL_RCLICKED handler

wxGTK: Applied patch for combo box SELECTED events (no longer get
lots of surplus events)

wxGTK: Applied patch for proper menu highlight colour detection in
wx.SystemSettings.

wxGTK: Committed scrollbar patch #1093339 which sends lineup, linedown
events based on intercepting the mouse down events.

wxGTK: Applied patch #1102789 which solved conflicts between wxWidgets
and GTK+'s context menu code.

wxGTK: Applied patch #1100327 for correct feedback from DND actions
(not all actions are allowed).

Fixed memory leak in wxGrid::UpdateAttr[Rows][Or][Cols] (patch 1104355)

For efficiency reasons, text controls no longer set the string for
each text updated event, but rather query for the string value only
when GetString is called from an event handler.

Added wx.SL_INVERSE style which will cause wx.Slider to invert the min
and max ends of the slider.

Several patches applied, such as #1111174, #1110252 and others, that
make the generic wx.TreeCtrl (used on wxGTK and wxMac) be more
conistent with the wxMSW native wx.TreeCtrl.

XRCed:
    * Edit->Locate command (Ctrl-L) for quick selection of items.
      Works with event-handling controls (buttons, text fields) but
      not with labels/sizers.
    * Some improvements: relative paths for files supplied as command-
      line argument work correctly, notebook panels are highlighted
      better.

wxMac: Fixed a long-standing issue where wxSlider controls with a
hardcoded size would misplace their labels behind the slider control.

wx.HtmlListBox fixed so calling RefreshLine(s) will cause the data for
that line to be refetched from the overridden methods in the derived
class.

The default DoGetBestSize now includes the difference (if any) between
the client size and total size of the window, (such as the size of
borders.)  Code that sets the client size using the best size, or that
added extra space to sizers to compensate for this bug may need to be
changed.

Can suppress themed notebook pages with the wxNB_NOPAGETHEME style or
setting system option msw.notebook.themed-background to 0.

wxSyledTextCtrl updated to use Scintilla 1.62.

Can now set the msw.window.no-clip-children system option to 1 to
eliminate weird refresh behaviour (delays between a window being
erased and repainted, giving a ghostly gradual-redraw effect). May be
a temporary 'fix' until properly fixed before 2.6.

wxMac:  Toolbar is now more native looking with borderless toolbar
buttons.

wxMac: Switched wx.Bitmap to use newer Quartz object types and APIs
internally.  This results in faster display and better alpha support.

Added wx.DatePickerCtrl.

wx.html.HtmlWindow now supports background images.

Added wx.lib.gestures module from Daniel Pozmanter which supports
using Mouse Gestures in an application.

wxGTK2: ENTER and LEAVE mouse events are now sent for multi-line text
controls.

wxMSW:  "Alt" key (VK_MENU) now results in WXK_ALT keyboard event, not
WXK_MENU

Added modules from Peter Yared and Morgan Hua that implement the wx
Doc/View framework in pure Python code.  See wx.lib.docview for the
base implementation and wx.lib.pydocview for Python-specific
extensions.  There are also a couple sample applications located in
samples/docview.

Added GetBitmap, GetIcon to wx.ImageList.

wxGTK wx.Button.SetLabel no longer invalidates/resets the font.

wx.Sizer.AddWindow, AddSizer, AddSpacer and etc. have now been
undeprecated at the request of Riaan Booysen, the Boa Constructor team
lead.  Boa needs them to help keep track of what kind of item is being
managed by the sizer.  They are now just simple compatibility aliases
for Add, and etc.

The old C++ version of the OGL lib is no longer built by default.  Use
the Python version in the wx.lib.ogl package instead.

The wx.iewin module is no longer built by default.  You can use the
wx.lib.iewin version instead.

Fixed wx.BufferedPaintDC for scrolled windows to work whether the
buffer is covering only the client area or the full virtual area of
the scrolled window.  By default it will assume that only the client
area is covered.  This is different than the old behavior so to
indicate that the entire virtual area is covered simply add a
style=wx.BUFFER_VIRTUAL_AREA parameter.

wx.gizmos.TreeListCtrl:  Add support for the EVT_TREE_ITEM_GETTOOLTIP
event.

Added Resize, SetRGBRect, Size, and GetOrFindMaskColour methods to
wx.Image.

Added wx.Rect.IsEmpty

wxGTK:
    - Corrected wx.ListBox selection handling
    - Corrected default button size handling for different themes
    - Corrected splitter sash size and look for different themes
    - Fixed keyboard input for dead-keys




2.5.3.1
-------
* 9-Nov-2004

wxMac focus and border refreshes corrected.

Updated internal PNG library.

wxMac fix for metal appearance on wx.ToolBar.

wx.grid.Grid fix allowing DoGetBestSize to be called before CreateGrid
(which means that a min size doesn't need to be specified.)

wxMac fix for not sending a native click to a control if it is not
enabled (does an enable itself)

Added wx.lib.ogl.DrawnShape, and fixed various little bugs in the new
OGL.

Added support to XRC and XRCed for the 3-state checkbox flags and also
for wx.ToggleButton.  Updated the generic window styles supported by
XRCed.

It is now possible to create "stock" buttons.  Basically this means
that you only have to provide one of the stock IDs (and either an
empty label or a label that matches the stock label) when creating the
button and wxWidgets will choose the stock label to go with it
automatically.  Additionally on the platforms that have a native
concept of a stock button (currently only GTK2) then the native stock
button will be used.  For example, the following will result in a
button with "Cancel" as the label and if run on wxGTK2 then there will
also be an image of a red X::

       b = wx.Button(parent, wx.ID_CANCEL)


Added wx.lib.ticker.Ticker class from Chris Mellon.

Fix some incorrect clipping regions in wxSTC on wxGTK.

Added wrapper for wx.grid.Grid.GetOrCreateCellAttr.

Removed my copy of distutils from the wxPython source tree.  Now that
I am no longer doing builds on Python 2.1 the newest distutils is no
longer needed.  (There is still one small bug in Python 2.2 distutils
on win32, but it is easily worked around.) This sovles the problem of
incorrect builds on some systems where the system installed distutils
has been patched to behave slightly differently, for example SuSE on
x86_64 or Chandler's build.

Updated to SWIG 1.3.22 (plus my patch.)  See wxPython/SWIG/README.txt
in the source tree if you need to use SWIG when building your own copy
of wxPython, or other extension modules that need to integrate with
the wxPython modules.

Added wx.Frame.RequestUserAttention which, if the platform supports it,
will do something (such as flash the task bar item) to suggest to the
user that they should look at that window.

"Fixed" wx.grid.Grid.SetDefaultEditor and SetDefaultRenderer by making
them register the editor or renderer for the "string" data type.

Added depth param to wx.Image.ConvertToBitmap.

Extended the wx.calendar.CalendarCtrl class with methods that get/set
a Python datetime or date object.  (These will only work with Python
2.3+) The methods are PySetDate, PyGetDate, PySetLowerDateLimit,
PySetUpperDateLimit, PySetDateRange, PyGetLowerDateLimit, and
PyGetUpperDateLimit.  Also, CalendarEvent was extended with PySetDate
and PyGetDate methods.

wxMSW: SetBackgroundColour on a wx.Choice or a wx.ComboBox will now
also set the colour of the dropdown.

wxMac: MessageDialog now supports wx.NO_DEFAULT style

wxMSW: added AssociateHandle and DissociateHandle to wx.Window

wxMac: fix for toolbar tooltips

wx.Sizer.Show (and Hide) now take an optional parameter specifying if
the item to be shown should be searched for recursively in subsizers,
and return a boolean value indicating if the item was found.

wxMSW: fixed MaximizeEvent generation in wx.Frame

wxMSW: fixed sending duplicate EVT_COMBOBOX events

Smoother time estimation updates in wx.ProgressDialog (patch 992813)

Made wx.Listbook events more consistent with wx.Notebook ones (patch
1001271)

Fixed rounding errors in variable status bar panes widths computation
(patch 1030021)

Added possibility to specify printer bin (patch 910272)

wxMSW: fixed wx.ListCtrl's SetWindowStyleFlag() to not remove
WS_VISIBLE; also refresh the control automatically (closes bug
1019440)

Added wx.Choicebook, yet another notebook-like control.

wxMSW: Make radiobutton tab behaviour the same on MSW as in standard
MSW app, i.e. tab into the activated, not necessarily the first radio
button.

Added limited support for wxEventLoop (you can't derive from a
wx.PyEventLoop version yet...)  Updated and moved the sample showing
how to replace the MainLoop to samples/mainloop/mainloop.py.

The C++ xrc lib has been moved out of contrib and into the core, so it
is always built by default.  wxPython's build has also changed
accordingly and will build the xrc module as part of the core set of
modules built by default.  If you were axplicitly using BUILD_XRC then
it will no longer be recognized as a build option, otherwise you
should notice no difference.

wxMac: Fixed radio toolbar buttons to correctly untoggle the others
when a new one is selected.

wxMac: Fixed GetLineLength and GetLineText for MLTE text controls

wxMac: wx.TaskBarIcon is implemented by allowing you to change the
app's icon on the Dock and also specifying a menu that should be
merged with the normal dock popup menu.  See the MigrationGuide for
more details and a warning.

Added wx.TopLevelWindow.IsActive() which tells you if the frame or
dialog is or contains the active window with the keyboard focus.

Added ability to create a font based on pixel size rather than point
size via the FontFromPixelSize constructor.

Updated the Scintilla used by StyledTextCtrl to version 1.61

Improved image HitTest for TreeListCtrl.

Added wx.App.IsMainLoopRunning.

wxGTK: Make wxComboBox spit out a bit fewer surplus events when
holding down the mouse button.

wxGTK: Enable key based navigation through notebook tabs as in the
native control with Left and right keys. Support for vetoing.

FloatCanvas updates from Chris Barker

PyPlot updates from Gordon Williams:
   - Added bar graph demo
   - Modified line end shape from round to square.
   - Removed FloatDCWrapper for conversion to ints and ints in
     arguments
   - Imported modules given leading underscore to name.
   - Added Cursor Line Tracking and User Point Labels.
   - Demo for Cursor Line Tracking and Point Labels.
   - Size of plot preview frame adjusted to show page better.
   - Added helper functions PositionUserToScreen and
     PositionScreenToUser in PlotCanvas.
   - Added functions GetClosestPoints (all curves) and GetClosestPoint
     (only closest curve) can be in either user coords or screen
     coords.

MaskedEdit updates from Will Sadkin:
    - Added '*' mask char that means "all ansii chars" (ords 32-255)
    - Added proper unicode support to masked controls and wx.tools.dbg
    - Fixed two reported missing import bugs introduced by package
      creation
    - Converted masked package doc strings to reST format for better
      epydoc support
    - lots of doc string improvements and function hiding to better
      reflect package's public contents.

Restructured the installer packages slightly to help facilitate having
multiple versions of wxPython installed at the same time.  See the
Migrarion Guide for more information.

Applied patch from Pim Van Heuven that modifies 4 files:
    - wxPython/demo/ListCtrl_edit.py (new demo)
    - wxPython/demo/Main.py (include new demo in demo app)
    - wxPython/wx/lib/mixins/listctrl.py (several improvements to
      TextEditMixin)
    - wxPython/wx/lib/wxpTag.py (some small fixes)

Added (thanks to Kevin Ollivier!) wrappers for wx.WebKitCtrl for the
OSX build.  Other platforms will raise an exception if you try to use
it.

wxPython on OSX can now be built in Unicode mode, can support multiple
version installs, and comes with an uninstaller script.





2.5.2.8
-------
* 27-Aug-2004

Predominantly a bug-fix release:

* Fixed fatal error due to improper wrapping of wx.FSFile.

* Fixed return type of EditableListBox.GetListCtrl

* Give generic tree and list controls a DoGetBestSize so they play
  nicer with sizers when there is no minimal size.

* Some tweaks in the demo and samples to correct layout, some
  flicker problems, and namespace use.

* Add wx.Image.ConvertAlphaToMask

* Minor corrections in wx.lib.dialogs

* wx.FileHistory constructor now accepts the documented 2nd
  parameter.

* Corrections for exceptions in the new ogl

* Fixed XRCed to not use reparenting of windows to implement caching
  of property panels, since Reparent on wxMac is not implemented.

* Add support for wxTAB_TRAVERSAL to the XRC handler for
  wxScrolledWindow.

* Add support for all wxListBox styles to the XRC handler for
  wxCheckListBox.

* Fix for wx.Listbook.DeleteAllPages to really delete everything.

* wxGTK2 now supports alpha blended bitmap drawing

* Made wx.grid.Grid play nicer with sizers.

* etc.




2.5.2.7
-------
* 14-Aug-2004

wx.ADJUST_MINSIZE is now the default behaviour for window items in
sizers.  This means that the item's GetMinSize and/or GetBestSize will
be called when calculating layout and the return value from that will
be used for the minimum size used by the sizer.  The wx.FIXED_MINSIZE
flag was added that will cause the sizer to use the old behaviour in
that it will *not* call the window's methods to determine the new best
size, instead the minsize that the window had when added to the sizer
(or the size the window was created with) will always be used.  Please
see the Sizers section in the Migration Guide for more details.

Added new MaskedEditControl code from Will Sadkin.  The modules are
now locaed in their own sub-package, wx.lib.masked.  Demos updated.

The changes that implemented the incompatible wx.DC methods in 2.5.1.5
have been reverted.  The wx.DC methods are now compatible with the 2.4
implementation.  In addition a set of renamed methods have been added
that take wx.Point and/or wx.Size objects instead of individual
parameters.

Added wx.lib.mixins.listctrl.TextEditMixin, a mixin class that allows
all columns of a wx.ListCtrl in report mode to be edited.

Deprecated the wx.iewin module.

Deprecated the wx.Sizer.AddWindow, AddSizer, AddSpacer methods as well
as their Insert* and Prepend* counterparts.

Added a generic StaticBitmap class in wx.lib.statbmp for the same
reasons that stattext was created, so it could be mouse sensitive on
all platforms like normal windows.  Also updated stattext.py and
buttons.py to handle attribute (font & colour) defaults and
inheritance the new way.  If you have custom controls of your own you
should review stattxt.py or one of the others to see how it is to be
done.

wx.InitAllImageHandlers is now an empty function that does nothing but
exist for backwards compatibility.  The C++ version is now called
automatically when wxPython is initialized.  Since all the handlers
are included in the wxWidgets shared library anyway, this imposes only
a very small amount of overhead and removes several unnecessary
problems.

Replaced wx/lib/pubsub.py with a version that uses weak references to
track the subscribers, plus other fixes/additions.  Thanks go to
Oliver Schoenborn and Robb Shecter.

wxGTK now uses gtk_init_check so wxPython can raise an exception if
there is no DISPLAY available or other initializaion problem.

wx.GetKeyState now has an implementation for wxGTK and is able to
detect the up/down or toggle state of modifier and toggle keys.

The LC_NUMERIC locale is now reset back to "C" (compatibility) when
running on wxGTK to work around the fact that GTK requires the locale
to be set to the system settings but Python depends on LC_NUMERIC
remaining compatible with "C".

Switched gizmos.TreeListCtrl to the newer version of the code from the
wxCode project.

OGL is dead! LONG LIVE OGL!  (Oops, sorry.  A bit of my dramatic side
leaked out there...)  The wx.ogl module has been deprecated in favor
of the new Python port of the OGL library located at wx.lib.ogl
contributed by Pierre Hjälm.  This will hopefully greatly extend the
life of OGL within wxPython by making it more easily maintainable and
less prone to getting rusty as there seems to be less and less
interest in maintaining the C++ version.  At this point there are just
a couple minor known compatibility differences, please see the
MigrationGuide file for details.

EVT_STC_POSCHANGED has been removed as it has been deprecated in
Scintilla for several releases now.

All the Window and GDI (pen, bitmap, etc.) class constructors and also
many toplevel functions and static methods will now check that a
wx.App object has already been created and will raise a
wx.PyNoAppError exception if not.

Added more default args as needed to allow most window types to be
constructed with only the parent window arg.  In some cases other args
may be required for normal operation, but they can usually be set
after construction.

Removed the deprecated ErrorDialogs and PythonBitmaps modules.  If you
were using these in your apps then please join wxPython-dev and assist
with a more modern reimplementation.

Added a new version (0.8.3) of FloatCanvas from Chris Barker.  It's now
in a subpackage of wx.lib.

It is now possible to change the tab traversal order of controls on a
panel or dialog.  For details see the new MoveAfterInTabOrder and
MoveBeforeInTabOrder methods of wx.Window.

Applied (and heavily modified) a patch from Eugene
<svip123@fastmail.fm> that allows the sample modules in the demo to be
edited and reloaded, all from within the demo.  You can switch back
and forth between the default and your edited version, and any errors
ocurring upon the reload are reported on the Demo tab.

Added a menu item in the demo that will open a PyShell window that has
the app and demo frame preloaded in the namespace.  This is another
good way to explore and play with the objects in the currently running
sample.  For example, load the Button sample and then do the following
in the PyShell::

        >>> b = frame.demoPage.GetChildren()[0]
        >>> for x in range(0, 500, 10):
        ...     b.Move((x, 50))
        ...     app.Yield(True)
        ...     wx.MilliSleep(10)


wxGTK: Applied wxNO_BORDER patch (#1098374) for text control and combo
box.



2.5.1.5    (the 'this is *not* a joke' release)
-----------------------------------------------
* 2-Apr-2004

(See also the MigrationGuide file for details about some of the
big changes that have happened in this release and how you should
adapt your code.)

The wxWindows project and library is now known as wxWidgets.  Please
see http://www.wxwindows.org/name.htm for more details.  This won't
really affect wxPython all that much, other than the fact that the
wxwindows.org domain name will be changing to wxwidgets.org, so mail
list, CVS, and etc. addresses will be changing.  We're going to try
and smooth the transition as much as possible, but I wanted you all to
be aware of this change if you run into any issues.


Many, many little fixes, changes and additions done as part of the move
to wxWidgets 2.5 that I have forgotten about.

Added wxMirrorDC.

Added wxIconLocation

Added Python wrappers and demos for the new wxVScrolledWindow,
wxVListBox, and wxHtmlListBox classes.

Added wrappers for wxBookCtrl and wxListbook.  wxNotebook now derives
from wxBookCtrl.

Added Gordon Williams' PyPlot module to the library, available as the
wx.lib.plot module.

I made a small but important change in the code that acquires the
Python Global Interpreter Lock to try and prevent deadlocks that can
happen when there are nested attempts to acquire the GIL.

The RPMs will now install menu items on Mandrake Linux in
Applications/Development/Tools for PyCrust, XRCed, etc.  The RPMs are
also installing icons and ``*.desktop`` items in the generic KDE and
GNOME locations, but I don't know yet if they are resulting in menu
items on non-Mandrake systems.  (It didn't automatically do it on my
RH-9 build box but I didn't chase it very far...)  If you have ideas
for how to improve the .spec file to work better and/or on more
distros please send me a patch.

The RPMs are now built on a fairly generic RH-9 box, and I have tested
installing them also on my main Mandrake 9.2 box.

There are some big changes in the OS X disk image.  The actual
Installer package now *only* installs the wxMac dynlibs, wxPython
extension modules and Python packages, and also the command-line tool
scripts. The remaining items (demo, samples, and application bundles
for the Demo, PyCrust and XRCed) are now top-level items in the disk
image (.dmg file) that users can just drag and drop to wherever they
want to put them.

The wxWave class has been renamed to wxSound, and now has a slightly
different API.

Updated the AnalogClockWindow with many enhancements from E. A. Tacão.

wxMac now has wx.ToggleButton!

wx.stc.StyledTextCtrl has been updated to version 1.58 of Scintilla.

To help with the wx.stc.StyledTextCtrl performance issues on wxMac
I've added a SetUseAntiAliasing method (and GetUseAntiAliasing too)
that will turn off the use of antialiased fonts in the wxSTC, allowing
it to bypass the slow text measuring routines and use the fast and
simple one instead.  By default the setting is turned off (on wxMac
only.)  When run on OSX the Py* apps have a new item on the Options
menu for controlling this setting if you would like to experiment with
it.

Updated wx.lib.calendar with many fixes and enhancements from Joerg
"Adi" Sieker.

Added wx.Display and wx.VideoMode.

AppleEvents can be handled by overriding wx.App methods MacOpenFile,
MacPrintFile, MacNewFile, and MacReopenApp.

Added wx.PlatformInfo which is a tuple containing strings that
describe the platform and build options of wxPython.  See the
MigrationGuide for more details.

Created a new extension module "activex" from Lindsay Mathieson's
newest wxActiveX_ class.  (The existing iewin module used an older
version of this code, but only exposed the wxIEHtmlWin class.)  This
new module will (in theory ;-) ) allow you to host arbitrary ActiveX
controls in a wx.Window, **without** requiring the use of the win32com
and other PyWin32 modules!  This should eliminate the cronic problems
that have resulted from minor mismatches in how PyWin32 handles the
GIL and tstate when making callbacks, etc.  The older iewin module
will be left in this release as the new stuff is not fully backwards
compatible, but you should migrate your code to the new IEHtmlWindow
in wx.lib.iewin, so the old one can be eventually removed.
Additionally, I've always considered that the wx.lib.activexwrapper
module is an ugly hack that I only included in the lib because I
couldn't figure out anything better.  Well now we have something that,
if it isn't already, has the potential to be better.  So consider
migrating away from using activexwrapper as well.  Please see the
MigrationGuide for more details on using the new module.

.. _wxActiveX: http://members.optusnet.com.au/~blackpaw1/wxactivex.html

Floats are allowed again as function parameters where ints are expected.




2.4.2.4
-------
* 1-Oct-2003

Use wxSTC in the demo for displaying the source code of the samples.

Lots of bug fixes and such from the wxWindows folks.

Added wxPython.lib.newevent from Miki Tebeka.  Its usage is
demonstrated in the Threads sample in the demo.

Updates to wxMaskedEditCtrl.

Added wxMaskedNumCtrl.

Added Chris Barker's FloatCanvas.



2.4.1.2
-------
* 19-Jun-2003

Added wxScrolledPanel from Will Sadkin

Added SetShape method to top level windows (e.g. wxFrame.)

Changed wxSWIG to not generate Python code using apply, (since it will
be deprecated in the future) wxSWIG will use ``spam(*args, **kw)`` syntax
instead.  Also changed the generated __repr__ methods to be a bit more
informative.

Made the version number information more robust and uh, informative.
Also added asserts to check that the major.minor versions of wxPython
and wxWindows match.

Added the new wx "renamer" package that will dynamically import from
the wxPython package and rename wxFooBar --> FooBar.  That means that
people can do imports without ``"import *"`` and can use names like
wx.Frame instead of wx.wxFrame.  This is phase 1 of a full transition
to the new namespace.

Updated Scintilla to 1.52.  I also changed it to use wxListCtrl
instead of wxListBox for the AutoComplete window, added the ability to
use custom bitmaps in the margin and in the AutoComplete windows, and
worked out how to do proper clipping of child windows on wxGTK.

Patrick O'Brien's PyCrust package has been renamed to Py and now
includes several new tools.  As part of the change the location of the
package has changed as well, it is now accessible as "from wxPython
import py" (or "from wx import py" using the new namespace.)  There
are still some transition modules in the wxPython.lib.PyCrust package
that will issue a warning and then import what is needed from the new
package.  These will be removed in a future release.

Added __nonzero__ method to wxTreeItemId, wxBitmap, wxImage, wxFont,
and most other classes that have an Ok or IsOK method.  This allows
code like "if obj: ..." to be the same as "if obj.IsOk(): ..."

Toolbars on wxMac can now have controls on them.

Added wxPython.lib.analogclock module based on samples that were
passed back and forth on wxPython-users a while back.

Added masked edit controls (wxPython.lib.maskededit) by Jeff Childers
and Will Sadkin.  Updated wxTimeCtrl to use MaskedEdit.

When the __class__ of a dead object is replaced with _wxPyDeadObject
the __del__ of the original class is now called first.

Added wxTreeListCtrl.  (Looks like a wxTreeCtrl embedded in a
wxListCtrl, but actually is just giving multiple columns to a
wxTreeCtrl.)

Added wxFutureCall, a subclass of wxTimer that makes it easy to delay
a call to any Python callable object.

Added wxPy versions of wxPrintPreview, wxPreviewFrame, and
wxPreviewControlBar so they can be derived from in Python and be able
to override the C++ virtual methods.

Simplified how the wxSizer methods are wrapped, changed the name of
the "option" parameter to "proportion" to match the docs ("option" is
still accepted for compatibility, but this will go away in a future
release,) SetItemMinSize can now take a wxSize (or 2-tuple) parameter,
and Spacers can be specified with a wxSize (or 2-tuple) parameter

Added wxCursorFromBits.





2.4.0.7
-------
* 24-Mar-2003

Gave up on generating a warning upon the use of the old true/false or
TRUE/FALSE values.

Fixed wxGenericTreeCtrl (used on wxGTK and wxMac for wxTreeCtrl) so
that it can successfully handle lots of nodes instead of overflowing
when the virtual height of the widget overflowed a 16-bit value.

Fixed the typemap that converts strings to wxColours to also accept
unicode.

Fixed problem where the wrong class name could sometimes be used for
OOR.

Fixed an interpreter lock problem in the __eq__ and __ne__ methods in
wxSize and etc.

Updated PyCrust to version 0.9

Instead of always logging C++ assertions, added wxPYAPP_ASSERT_LOG
flag to turn it on.  In most cases turning it into an exception (the
default behavior) is enough.  See below in the 2.3.4.1 notes for more
details.




2.4.0.6 (a.k.a. the I'm so stupid release)
------------------------------------------
* 11-Mar-2003

The new deprecation class for the old true/false symbols can now be
returned from OnInit.  And I promise to be sure I am testing what I
think I am testing in the future...



2.4.0.5 (a.k.a. the blame it on Kevin release)
----------------------------------------------
* 7-Mar-2003

A few little but annoying bug fixes.

Updated pycolourchooser.

Updated to 0.9b of PyCrust.



2.4.0.4
-------
* 7-Mar-2003

Added missing wxRect methods

Add OOR support for wxApp objects too.

Added wxCursorFromImage, which works on wxMSW and wxGTK so far.

All platforms now send EVT_DESTROY_WINDOW.  Be warned that at the time
the event is sent the window is in the process of being deconstructed,
and so calling some (most?) methods of the window itself may cause
problems.

Fixed SF Bug #689481, a method in the OGL wrappers was using the wrong
return type.

Fixed SF Bug #689958, an endless loop in printout.py.

Added EVT_WINDOW_CREATE_ID and EVT_WINDOW_DESTROY_ID so these events
can be associated with a specific window ID and more easily caught by
the parent window.

Fixed copy-paste error in wxListCtrl.GetFirstSelected.

Added missing Init method (and an overloading wrapper) to wxLocale
wrapper.

Added a wxBitmap.SetMaskColour convenience method.

Changed how the dynamic event tables (used for all Python wx classes,
C++ wx classes typically use static event tables) are searched such
that they behave from a Python perspective more like the static tables
in C++.  Namely that if there are identical event bindings in a base
Python class and a derived Python class that the one in the derived
class will be found first and that if Skip is called that the one in
the base class will still be found instead of skipping directly to the
static stable in the C++ class.

Switched to using True/False in the wxPython lib and demo instead of
true/false or TRUE/FALSE to prepare for the new boolean type and
constants being added to Python.  Added code to wx.py to test for the
existence of the new constants and to create suitable values if not
present.

Added some static wxApp functions that help with integration with the
Mac UI.  They are no-ops on other platforms so it doesn't hurt to
always call them.  The functions are::

       wxApp_GetMacDefaultEncodingIsPC
       wxApp_GetMacSupportPCMenuShortcuts
       wxApp_GetMacAboutMenuItemId
       wxApp_GetMacPreferencesMenuItemId
       wxApp_GetMacExitMenuItemId
       wxApp_GetMacHelpMenuTitleName
       wxApp_SetMacDefaultEncodingIsPC
       wxApp_SetMacSupportPCMenuShortcuts
       wxApp_SetMacAboutMenuItemId
       wxApp_SetMacPreferencesMenuItemId
       wxApp_SetMacExitMenuItemId
       wxApp_SetMacHelpMenuTitleName

Refactored, enhanced and added capabilities for the DrawXXXList
functions, inspired by code from Chris Barker.

The wxWindows .mo language catalog files are now installed in a
subdirectory of the wxPython package dir on MSW since that platform
doesn't have a standard place for them.

Added missing deselect methods for wxGrid.

Fixed typemaps for wxGridCellCoordsArray.

Updated to the 0.9a version of PyCrust



2.4.0.2
-------
* 23-Jan-2003

Several bug fixes.

Added wxIntCtrl from Will Sadkin.

Added wxPyColourChooser by Michael Gilfix.




2.4.0.1
-------
* 10-Jan-2003

No major new features since 2.3.4.2, mostly bug fixes and minor
enhancements.

Added function wrappers for the common dialogs from Kevin Altis.  See
wxPython/lib/dialogs.py for more details.



2.3.4.2
-------
* 21-Dec-2002

Various bug fixes.



2.3.4.1
-------
* 18-Dec-2002

Updated XRCed and wxTimeCtrl contribs.

Show a couple new wxGrid features in the demo.

Several bug fixes in wxWindows.

Added wxHtmlFilter.

wxASSERT and related C++ runtime diagnostics are now converted to
Python exceptions.  When an assert happens a wxPyAssertionError
(which derives from AssertionError) exception is created and when
control returns back to the Python code that invoked the C++ API it
will be raised.  The same exception restrictions are in place as
before, namely that exceptions can't cross from one Python layer
through C++ to another Python layer.  That simply means that if you
want to catch wxPyAssertionError or any other exception that you need
to do it before control returns to C++ at the end of your event
handler or callback code.  There is some test code in demo/wxButton.py
you can use to play with this new feature.

Added some methods to wxApp (SetAssertMode and GetAssertMode) that let
you control how C++ assertions are processed.  Valid modes are:
wxPYAPP_ASSERT_SUPPRESS, wxPYAPP_ASSERT_EXCEPTION, and
wxPYAPP_ASSERT_DIALOG.  Using _SUPPRESS will give you behavior like
the old "final" builds and the assert will be ignored, _EXCEPTION is
the new default described above, and _DIALOG is like the default in
2.3.3.1 and prior "hybrid" builds.  You can also combine _EXCEPTION
and _DIALOG if you wish, although I don't know why you would.

You can now overload OnInitGui, OnExit and OnAssert in your classes
derived from wxApp.

Added GetSelectedCells, GetSelectionBlockTopLeft,
GetSelectionBlockBottomRight, GetSelectedRows, GetSelectedCols methods
to wxGrid.

Added Python == and != operators for some basic classes

Fixed the Python wrappers for wxInputStream so they no longer block
when reading from a wxProcess on wxGTK.  They now work more or less as
they did before 2.3.3.1 but the dual meaning of eof() has been
removed.  There is now a CanRead() method that lets you know if there
is data waiting to be read from the pipe.

Fixed method name clash in wxIEHtmlWin, renamed Refresh to RefreshPage.

Added Throbber from Cliff Wells to the library and the demo.

Windows installer prompts to uninstall old version first.

Added wxPython.lib.evtmgr by Robb Shecter, which is an easier, more
"Pythonic" and more OO method of registering handlers for wxWindows
events using the Publish/Subscribe pattern.

Added wxPython.lib.popupctl by Gerrit van Dyk which is a combobox-like
gizmo for popping up arbitrary controls.  It is currently using
wxDialog because of some issues with wxPopupWindow...

Added wxPython.lib.gridmovers by Gerrit van Dyk which facilitates the
dragging of columns and/or rows in a wxGrid.

Added wxPython.lib.multisash by Gerrit van Dyk which is a nice
implementation of allowing the user to split a window any number of
times either horizontally or vertically, and to close the split off
windows when desired.

Added helpviewer tool that displays HTML books similarly to how MS
HTMLHelp viewer does.  Changed how the wxPythonDocs tarball is built
and added a script to launch the doc viewer.




2.3.3.1
-------
* 19-Sep-2002

Added wxSplashScreen.

Added wxGenericDirCtrl.

Added wxMultiChoiceDialog.

The calltip window and autocomplete window in wxSTC will now use a
wxPopupWindow if available on the platform (and functioning correctly)
so they can extend beyond the client area of the STC if needed.

Finished wrapping and providing typemaps for wxInputStream and also
added the stream ctor and other methods for wxImage so images can now
be loaded from any Python "file-like" object.

Changed the img2py tool to use PNG instead of XPM for embedding image
data in Python source code, and the generated code now uses streams to
convert the image data to wxImage, wxBitmap, or wxIcon.

Added the wxPython.lib.rcsizer module which contains RowColSizer.
This sizer is based on code from Niki Spahiev and lets you specify a
row and column for each item, as well as optional column or row
spanning.  Cells with no item assigned to it are just left blank.
Stretchable rows or columns are specified and work the same as in
wxFlexGridSizer.

Updated XRCed from Roman Rolinsky

Added wxBufferedDC.

Upgraded wxSTC from Scintilla 1.40 to Scintilla 1.45, and then again
to version 1.47, and one more time to 1.48! <wink>

UNICODE!
    wxWindows/wxPython can be compiled with unicode support enabled or
    disabled.  Previous to wxPython 2.3.3 non-unicode mode was always
    used.  Starting with 2.3.3 either mode is supported, but only if
    it is also available in wxWindows on the platform.  Currently
    wxWindows only supports unicode on MS Windows platforms, but with
    the recent release of GTK+ 2.0 it is only a matter of time until
    it can be done on wxGTK (Linux and other unixes) as well.

    Unicode works best on platforms in the NT branch of the Windows
    family tree (NT, win2k, XP) but it is now also possible to use the
    same unicode binaries on win95/98/ME platforms as well!  This is
    done by using a special library and DLL with the application
    called MSLU, (Microsoft Layer for Unicode).  It simply gets out of
    the way if the app is run on an NT box, otherwise if run on a
    win9x box it loads a special DLL that provides the unicode
    versions of the windows API.  So far I have not been able to get
    this to work perfectly on win9x.  Most things work fine but
    wxTaskBarIcon for example will cause a crash if used with the
    unicode build on win95.

    So how do you use it?  It's very simple.  When unicode is enabled,
    then all functions and methods in wxPython that return a wxString
    from the C++ function will return a Python unicode object, and
    parameters to C++ functions/methods that expect a wxString can
    accept either a Python string or unicode object.  If a string
    object is passed then it will be decoded into unicode using the
    converter pointed to by wxConvCurrent, which will use the default
    system encoding.  If you need to use a string in some other
    encoding then you should convert it to unicode using the Python
    codecs first and then pass the unicode string to the wxPython
    method.

Added wxListCtrlAutoWidthMixin from Erik Westra.

Added wxIconBundle and wxTopLevelWindow.SetIcons.

Added wxLocale and wxEncodingConverter.

A little black magic...  When the C++ object (for a window or
whatever) is deleted there is no way to force the Python shadow object
to also be destroyed and clean up all references to it.  This leads to
crashes if the shadow object tries to call a method with the old C++
pointer.  The black magic I've done is to replace the __class__ in the
Python instance object with a class that raises an exception whenever
a method call (or other attribute access) is attempted.  This works
for any class that is OOR aware.

Added OOR support for wxGridCellRenderer, wxGridCellEditor,
wxGridCellAttr, wxGridCellAttrProvider, wxGridTableBase and their
derived classes.

Added wxImage.GetDataBuffer which returns an in-place edit buffer of
the image data.  (Patch #546009)

Added a sample that shows how to embed wxPython in a wxWindows C++
application.

Added wxPyWindow, wxPyPanel and wxPyControl which are just like their
wx counterparts except they allow some of the more common C++ virtual
methods to be overridden in Python derived classes.  The methods
supported are:

- DoMoveWindow
- DoSetSize
- DoSetClientSize
- DoSetVirtualSize
- DoGetSize
- DoGetClientSize
- DoGetPosition
- DoGetVirtualSize
- DoGetBestSize
- InitDialog
- TransferDataFromWindow
- TransferDataToWindow
- Validate
- AcceptsFocus
- AcceptsFocusFromKeyboard
- GetMaxSize
- AddChild
- RemoveChild

If there are other methods that you think should be supported
please let me know.

Changed wxGenButton to derive from wxPyControl and overload
DoGetBestSize and AcceptsFocus.

Added wxArtProvider.

Added wxCallAfter which is a helper function that registers a function
(or any callable Python object) to be called once the next time there
are no pending events.  This is useful for when you need to do
something but it can't be done during the current event handler.  The
implementation is very simple, see wxPython/wx.py.

Fixed a boatload of reference leaks.

Added a demo of using a sizer in a wxScrolledWindow, in effect
creating a ScrolledPanel.

Added a sample to the demo that shows how to use radio menu items, and
other menu stuff.

Added wxIEHtmlWin.  This is essentially the same as using IE with the
ActiveXWrapper already in the library, but it is implemented all in
C++ and therefore does not need any of the modules from win32all and
so it is less fragile in the face of changes.

Fixed the ActiveXWrapper problem.  Looks like when the win32com
modules make a "callback" that they (incorrectly, IMHO) allocate a
transient thread state structure.  Since wxPython is now saving
tstates for it's own callbacks it ended up using garbage after
win32com got rid of the temporary tstate...

Added a generic static text control to wxPython.lib.stattext.  This is
so things like Boa and PythonCard can have a static text that can
respond to mouse events and etc.

Changed the wxDateTime.Parse* methods to return an int that will be -1
on failure, and the index where parsing stopped otherwise.

Moved tools to be a Python package in wxPython.tools, added scripts to
import and launch each tool.  This will let you import and use the
tools in your own scripts or apps as needed.  On Linux and OS X the
tool scripts are installed to {prefix}/bin so you should be able to
easily launch them from the command line.  For example, PyCrust can be
started with just the "pycrust" command.

Added a sample to the demo that catches various key events and
displays the details of the event.

Added wxWizard, wxWizardPage, wxWizardPageSimple and wxPyWizardPage.

Added wxXmlResourceHandler which allows you to create custom handlers
for nonstandard class types in XRC resources.  See the demo for an
example.

Added wxPython.lib.mixins.rubberband module from Robb Shecter.

Added wxTimeCtrl from Will Sadkin.




2.3.2.1
-------
* 20-Dec-2001

Changed (again) how the Python global interpreter lock is handled as
well as the Python thread state.  This time it works on SMP machines
without barfing and is also still compatible with Python debuggers.

Added some patches from library contributors.



2.3.2
-----
* 11-Dec-2001

Added EVT_HELP, EVT_HELP_RANGE, EVT_DETAILED_HELP,
EVT_DETAILED_HELP_RANGE, EVT_CONTEXT_MENU, wxHelpEvent,
wxContextMenuEvent, wxContextHelp, wxContextHelpButton, wxTipWindow,
and a demo to show them in action.

Deprecated PyShell and PyShellWindow, added a snapshot of PyCrust (see
http://sourceforge.net/projects/pycrust/. )

Added the new virtual list capabilities to wxListCtrl.

Added a wxSTC style editor from Riaan Booysen to the sample apps.

Added XRCed to the wxPython Tools directory, contributed by Roman
Rolinsky.

Added a new "constructor" to most of the window classes that calls the
default C++ constructor, (the one with no parameters) and also added the
corresponding  Create(...) method.  This allows you to do a 2-step
creation of windows which is sometimes required for doing things such
as setting extended style flags before the window is created, or for
passing the object to the XRC resource system to be created from the
resource.  The name of the new "constructor" is the original name of
the class with a "Pre" in it.  For example, wxPreWindow, wxPreFrame,
etc.

Updated to version 1.40 of Scintilla and updated wxStyledTextCtrl
accordingly.  While doing this update I dropped the wxLB_SORT style
from the wxListBox created for the AutoComplete functionality.  This
means that you will have to sort the keyword lists yourself, but you
are free to do case sensitive or case insensitive sorts and set the
wxSTC flag accordingly.

Updated wxColumnSorterMixin to also be able to place sort icons on the
column headers, and updated the wxListCtrl demo to show it off by
using wxColumnSorterMixin.

Added wxGenBitmapTextButton, TablePrint, etc. contribs from Lorne White.

Added wxNativeFontInfo and wxFontMapper.

Added pySketch to the samples.

Significantly changed how the Python interpreter lock and thread state
are managed, which should fix the problem of running on a
multi-processor machine.

Added wxPyLog so log targets can be created in Python to handle log
messages however is wished.  See demo/Main.py for an example.

Added wxFindReplaceDialog.

The second phase of OOR is implemented for wxEvtHandler, wxSizer,
wxShape and derived classes.  This means that functions and methods
that return an object derived from wxEvtHandler that was originally
created in Python, will return the original Python object (if it still
exists) instead of letting SWIG wrap a new shadow object around the
original C++ pointer.

Added some optimization methods to wxDC: GetBoundingBox, DrawLineList,
DrawPointList.

Added a set of sophisticated Error Dialogs from Chris Fama.

Added wxRightTextCtrl from Josu Oyanguren to wxPython.lib for aligning
text in a wxTextCtrl to the right side.

Added wxURLDataObject and an example showing drag and drop of URLs to
and from web browsers.  It's still not 100% bullet-proof for all types
of browsers, but it works for the majority of cases with the popular
browsers on Windows.  On wxGTK it seems that only Netscape 4.x works,
if anybody has any suggestions about this please bring it up on the
wx-dev list.

Added wxStopWatch.

Added wxMimeTypesManager and wxFileType.

Passing None for the handler parameter to one of the EVT_** functions
will now Disconnect the event.

Added wxPopupWindow and wxPopupTransientWindow.

Added wxFileHistory.

Added wxDynamicSashWindow, which allows you to endlessly split windows
by dragging a little tab next to the scrollbars.  Added a demo to show
this and also the ability of multiple wxStyledTextCtrls to share the
same document.

Added wxEditableListBox gizmo.

Updated wxEditor with lots of enhancements from Steve Howell and Adam
Feuer.

Added the "SplitTree gizmos" which are a collection of classes that
were designed to operate together and provide a tree control with
additional columns for each item.  The classes are
wxRemotelyScrolledTreeCtrl, wxTreeCompanionWindow,
wxThinSplitterWindow, and wxSplitterScrolledWindow, some of which may
also be useful by themselves.

Added wxDllWidget from Vaclav Slavik which allows wx widgets derived
from wxWindow to be loaded from a C++ .dll (or .so) and be used in a
wxPython program, without the widget having to be SWIGged first.  The
visible API of the widget is limited to wxWindow methods plus a
SendCommand method, but it is still quite powerful.  See
wxPython/contrib/dllwidget and wxPython/demo/dllwidget for more
details.




2.3.1
-----
* 10-Jul-2001

Added EVT_GRID_EDITOR_CREATED and wxGridEditorCreatedEvent so the user
code can get access to the edit control when it is created, (to push
on a custom event handler for example.)

Added wxTextAttr class and SetStyle, SetDefaultStyle and
GetDefaultStyle methods to wxTextCtrl.

Added ability to use xml resource files.  Still need to add ability to
subclass wxXmlResourceHandler, etc...

Added wxGridAutoEditMixin to the mixins library package.

Made ColourSelect be derived from wxButton.

Fixed img2py to work correctly with Python 2.1.

Added enhanced wxVTKRenderWindow by Prabhu Ramachandran



2.3.0
-----
* 22-May-2001

Removed initial startup dependency on the OpenGL DLLs so only the
glcanvasc.pyd depends on them, (on wxMSW.)

Changed wxFont, wxPen, wxBrush to not implicitly use the
wxThe[Font|Pen|Brush]List objects behind the scenes, but to use normal
ctor and dtors.

Exposed the wxThe[Font|Pen|Brush]List to wxPython.

Also added wxTheColourDatabase and added a library module (in the
wxPython.lib.colourdb module) to load LOTS more colour names into the
colour database.

Added wxWakeUpMainThread, wxMutexGuiEnter, wxMutexGuiLeave,
wxMutexGuiLocker and wxThread_IsMain to assist with dealing with GUI
access from non-GUI threads.

wxPyOnDemandOutputWindow is now (more) thread safe if non-GUI threads
use print, sys.stdout.write, etc.

Added CreateTextSizer and CreateButtonSizer to wxDialog

Added wxPython/lib/infoframe.py from Chris Fama.  It contains a class
that can be used in place of wxPyOnDemandOutputWindow.

Added colourselect.py, imagebrowser.py and an updated calendar.py to
wxPython/lib from Lorne White.

Added patch to wxPoint_LIST_helper from Tim Hochberg that should make
it gobs faster in certain situations.

Added tools that will take an image file in a wx supported format and
convert it to data embedded in a Python source file.  The image is
converted to XPM format which is essentially a list of strings
containing info about each pixel.  The image's transparency mask is
included, if there is one, or a mask can be added if a mask colour is
specified on the command line.  It is then pickled and optionally
compressed and written to a Python source file along with functions to
convert it to either a wxBitmap or a wxImage.  See
wxPython/demo/images.py for examples, and wxPython/Tools/img2py.py for
the implementation.

Fixed wxStyledTextCtrl to be much faster on wxGTK.  There was some
experimental code that got left in place that ended up causing way too
many refreshes.

A couple more hacks in my_distutils.py so wxPython can be built with
the distutils that comes with Python 2.1.

Added a ton of missing methods for wxPrintData.

Switched to InnoSetup for MSW distributions.

Added wxToggleButton.

Fixed bug that prevented wxTreeCtrl.OnCompareItems from being called.

Added some methods to wxGrid:
      GetCellHighlightPenWidth
      GetCellHighlightROPenWidth
      SetCellHighlightPenWidth
      SetCellHighlightROPenWidth
      GetGridWindow
      GetGridRowLabelWindow
      GetGridColLabelWindow
      GetGridCornerLabelWindow

Added wxGetClientDisplayRect which on wxMSW returns a wxRect
representing the area on screen not occupied by the taskbar and such.
On other platforms it is equivallent to wxGetDisplaySize.

OOR:
   Implemented the first phase of OOR (Original Object Return).  See
   the text in the demo for more details of what this means, but in a
   nutshell methods such as wxWindow.GetParent or FindWindowById will
   now return a shadow object of the proper type if it can.  By
   "proper type" I mean that if the wxWindow pointer returned from
   FindWindowById really points to a wxButton then the Python object
   constructed will be of a wxButtonPtr class instead of wxWindowPtr
   as before.  This should reduce or eliminiate the need for
   wxPyTypeCast.  (Woo Hoo!)  The objects returned are still not the
   original Python object, but that is the next step.  (Although it
   will probably only work on Python 2.1 and beyond because it will
   use weak references.)

   This first phase of the OOR plan is fairly significant and has
   required a lot of changes all over wxPython, most of which should
   be transparent to you, however I'm not 100% sure that it didn't
   introduce any new bugs that are hiding somewhere and didn't get
   stomped on during my testing.  So please be sure to test everything
   thoroughly when you install this version and be sure to report any
   object-type related oddities to me.


There is now a wxObject class that most other classes derive from like
in C++, but the methods provided don't really match but are wxPython
specific.  It could have been added long ago but OOR required it so it
finally got done.

Finally added wxPyLineShape.GetLineControlPoints, which has been on my
list for a while.  The above OOR modification made this easier.

Fixed the __cmp__ methods for wxPoint and others.

Added wxWave.

Added the wxPython.lib.mixins package to the library, it is where
useful mix-in classes can be placed.  Currently there is one to help
make the columns in a wxListCtrl sortable, and the MagicIMageList from
Mike Fletcher.  If you have any custom code that can be factored out
of existing classes into a mix-in that would be useful to others
please send it to me for inclusion in this package.

Added a few little sample applications to help newbies to get started
by having smaller functional apps to play with.  They can be found in
wxPython/samples.




2.2.7
-----
* 19-Jun-2001

No changes happened in the Python wrappers for this release, only
changes and fixes in the wxWindows library.



2.2.5
-----
* 30-Jan-2001

New typemaps for wxString when compiling for Python 2.0 and beyond
that allow Unicode objects to be passed as well as String objects.  If
a Unicode object is passed PyString_AsStringAndSize is used to convert
it to a wxString using the default encoding.

Fixed the generic buttons so tool tips work for them.

Fixed a bug in the demo's tree control.

Added a listbox to the listbox demo that shows how to find items with
a matching prefix as keys are typed.

Added code to the wxListCtrl demo to show how to get text from a
column in report mode.

Added code to the toolbar demo to clear the long help from the status
bar after 2 seconds.

Added wxJoystick.

Fixed wxTimer so it can be used as described in the docs, either with
a Notify method in a subclass, or sending an event to a wxEvtHandler
object, (usually a window.)

Added wxNotifyEvent.Allow()

Fixed GOBS of reference leaks.

Massive code changes and cleanup to allow wxPython to be split into
multiple extension modules again.  A Python CObject is used to allow
the "export" of SWIG functions and other common helper functions from
the wxc module to other modules, even if they are in separate shared
libraries.  Should also be usable from 3rd party code, just include
wxPython/src/export.h

Changed the default setup so the following are built as separate
extension modules:  calendar, glcanvas, grid, html, ogl, stc, and
utils.  Will probably add more later.

Changed the wxPrinterDC to use the new constructor taking a
wxPrintData object.  The old ctor is still there using the
wxPrinterDC2 name.

Added wxPython.lib.anchors.py from Riaan Booysen.  It contains a class
that implements Delphi's Anchors with wxLayoutConstraints.

Added wxPython.lib.fancytext from Timothy Hochberg.

Changed the GenericButtons to send their event in idle time, so the
mouse won't be captured when the event handler is called.

Added wxPython.lib.rpcMixin from Greg Landrum, although it's not
integrated with the demo yet.  It allows a wxPython GUI to be an
XML-RPC server.



New in 2.2.2
------------
* 26-Oct-2000

Significantly changed how the wxStyledtextCtrl code that wraps
Scintilla is implemented.  Most of it is now automatically generated
from an interface definition file provided by Scintilla.  This means
that it will be much easier to stay in sync with new Scintilla
releases, but also means that some of the method and identifier names
have changed.  See wxPython/demo/data/stc.h for a copy of the C++
interface from which the Python interface is generated.  There is now
some inline documentation in that file that should really help explain
how things work.

I am now using the Python Distutils to build wxPython and to make some
of the distribution files.  (See http://www.python.org/sigs/distutils-sig/)
This means no more messing with my kludgy build.py/Makefile hack,
builds will be more consistent with other Python extensions that also
use Distutils, and will hopefully make wxPython easier to build for
platforms where there have been troubles before.  If you are building
wxPython for Python 1.5.2 or for 1.6, then you will need to get and
install version 1.0 of Distutils from the website above.  If you are
using Python 2.0 then you already have it.

Added wxInputStream and the wxFileSystem family of classes,
contributed by Joerg Baumann.

Added wxProcess and support for it to wxExecute.  wxProcess lets you
get notified when an asynchronous child process terminates, and also to
get input/output streams for the child process's stdout, stderr and
stdin.

Removed the old python sizers.

Added __add__, __sub__ and __cmp__ (equality check only) for wxPoint
and wxRealPoint.

Changed the build to make one big extension module instead of one for
the core and each contrib.  This allowed me to do away with the
libwxPyHelpers.so on unix systems.

Lots of little fixes here and there.

Some hacks on wxGTK to try and make the AutoComplete listbox in the
wxStyledTextCtrl to behave better.  It's still not as nice as on
wxMSW, but at least it's a bit more usable now.




New in 2.2.1
------------
* 22-Aug-2000

Various tweaks, fixes, missing methods, etc.

Added example use of wxTaskBarIcon to the demo.



New in 2.2.0
------------
* 17-Jul-2000

Added wxLog and friends.

Added wxFrame.ShowFullScreen for MSW.

Added PyShellWindow to the wxPython.lib package.



New in 2.1.16
-------------
* 12-Jun-2000

Added an attribute named labelDelta to the generic buttons that
specifies how far to offset the label when the button is in the
depressed state.

Added wxTipProvider and friends.  See the demo for an example.

wxGrid can now change the cell highlight colour.

Added wxDragImage.

Fixed printing on wxGTK.

Added wxDateTime, wxTimeSpan, and wxDateSpan to wxPython.utils.

Added wxCalendarCtrl.

WARNING: A while back I asked what should be done about the Magic
Method Names.  (Methods that are automatically turned into event
handlers by virtue of their name.)  The consensus was that it is more
confusing to have them than to try and expand them to have greater
coverage.  I am finally getting around to removing the code that
generates the event binding.  This means that if you are using any of
the following method names without a EVT_* call that you need to
modify your code to add the EVT_* to hook the event to the method.

- OnChar
- OnSize
- OnEraseBackground
- OnSysColourChanged
- OnInitDialog
- OnPaint
- OnIdle
- OnActivate
- OnMenuHighlight
- OnCloseWindow
- OnScroll

Added wxSpinCtrl.




New in 2.1.15
-------------
* 25-Apr-2000

Fixed wxTreeCtrl.HitTest to return both the tree item as well as the
flags that clairify where the click was in relation to the item.

Fixed thread state problem in wxTreeCtrl.GetBoundingBox and
GetSelections.

Fixed some problems in OGL.  Also wxShape.SetClientData and
.GetClientData can now deal with Python objects.

Added wxListCtrl.SortItems and changed the demo to show how to use it.

Plugged a memory leak.

Wrapped the new wxGrid and friends.  The old wxGrid class is no longer
available.  There are some incompatibilities, and unfortunately the
new classes are not documented yet, (however the methods are more
consistent with each other now so you may be able to guess pretty
good...)

Updated filebrowsebutton.py and calendar.py with changes from their
authors.  There is now a FileBrowseButtonWithHistory class (what a
mouthful!) and wxCalendar has printing support.

Added ActiveXWrapper to the library, and some good demos of it too.
It works great for embedding a COM (a.k.a OCX, a.k.a ActiveX) control
in a window and calling its methods.  It actually creates a new class
on the fly that derives from wxWindow, the COM CoClass and others
needed to make it all work.  The resulting class can be instantiated
just like wxWindow, used in sizers, etc.  It also responds to all COM
method calls, properties, etc., and if the class or a mix-in has
matching method names, then the COM events will be propagated back to
them.

Created a typemap that allows a string to be used for parameters
expecting a wxColour type.  The string is either a colour name as
defined in the wxColourDatabase, or a colour spec of the form
"#RRGGBB".  See the wxStyledTextCtrl demo for an example.

I almost forgot to mention the wxStyledTextCtrl!  Yes, the
wxStyledTextCtrl is finally in wxPython!!  (And the crowd goes
wild...)   There's no documentaTion yet (the crowd boos and hisses...)
but I've included a very readable source file in the
wxPython/demo/data directory, a couple fairly good examples, and you
can also refer to the Scintilla documentation at
http://www.scintilla.org/ScintillaDoc.html to help fill in the gaps
until the docs are done.  (The croud murmers contentedly as the tool
provider smiles convincingly and removes his flame-proof suit.)




What's new in 2.1.13
--------------------
* 3-Feb-2000

Skipped a version number to match what has been released for wxGTK.

Updated wxMVCTree and added a demo for it, also fixed layout on GTK
and some flicker problems.

Added a wrapper class for the Visualization ToolKit (or VTK) in the
wxPython.lib.vtk module.  (http://www.kitware.com/)

Fixed wxTreeCtrl.SetItemImage and GetItemImage to recognise the new
"which" parameter.

Added wxPython.lib.spashscreen from Mike Fletcher.

Added wxPython.lib.filebrowsebutton also from Mike Fletcher.

Renamed wxTreeCtrl.GetParent to GetItemParent to avoid a name clash
with wxWindow.GetParent.

Added wxIntersectRect to compute the intersection of two wxRect's.
It is used like this::

   intersect = wxIntersectRect(rect1, rect2)

If r1 and r2 don't intersect then None is returned, otherwise the
rectangle representing the intersection is returned.

Some bug fixes for Clipboard and Drag-n-Drop.

Rotated text!!!  WooHoo!  (See wxDC.DrawRotatedText())

Added a set of Generic Buttons to the library.  These are simple
window classes that look and act like native buttons, but you can have
a bit more control over them.  The bezel width can be set in addition
to colours, fonts, etc.  There is a ToggleButton as well as Bitmap
versions too.  They should also serve as a good example of how to
create your own classes derived from wxControl.

The C++ wxToolBar classes have been redone, and so have the wxPython
wrappers.  There have been slight modifications to some of the methods
but shouldn't impact anybody too much.  I took the opportunity to add
support for setting user data on each toolbar tool.  The new AddTool
methods look like this::

        def AddTool(ID,
                    bitmap,
                    pushedBitmap = wxNullBitmap,
                    toggle = FALSE,
                    clientData = NULL,
                    shortHelpString = "",
                    longHelpString = "")

        def AddSimpleTool(ID,
                          bitmap,
                          shortHelpString = "",
                          longHelpString = "",
                          toggle=FALSE)


There are also corresponding InsertTool and InsertSimpleTool methods
that additionally take an integer position as the first parameter.

Added a wrapper for the new PCX and TIFF ImageHandlers.

wxRect now simulates attributes named left, right, top and bottom.

Removed all non wx stuff from the glcanvas module since DA's PyOpenGL
is better and compatible with the wxGLCanvas.  You can get it at
http://starship.python.net:9673/crew/da/Code/PyOpenGL.

Added some missing EVT functions.

Added Dirk Holtwic's editor classes to the wxPython.lib.editor
package.

Changed all the "LIST" parameter names to "choices" to match the docs.

More fixes for the wxFloatBar, and it now works on wxGTK even better
than wxMSW!  (The feat is accomplished by using the wxTB_DOCKABLE
style flag instead of trying to float it ourselves.)




What's new in 2.1.11
--------------------
* 13-Nov-1999

Skipped a few version numbers so wxMSW, wxGTK and wxPython are all
synchronized.

wxImage.SetData now makes a copy of the image data before giving it to
wxImage.  I mistakenly thought that wxImage would copy the data
itself.

Fixed wxMSW's notebook so the pages get their size set as they are
being added.  This should remove the need for our
wxNotebook.ResizeChildren hack.

wxPanels now support AutoLayout, and wxNotebooks and wxSplitterWindows
no longer tell their children to Layout() themselves.  This will
probably only effect you if you have a wxWindow with AutoLayout inside
a notebook or splitter.  If so, either change it to a wxPanel or add
an EVT_SIZE handler that calls Layout().

Fixed deadlock problem that happened when using threads.

Added new HTML printing classes.

Added wxWindow.GetHandle

Apparently wxMouseEvent.Position has been deprecated in wxWindows as
it is no longer available by default.  You can use GetPositionTuple
(returning a tuple with x,y) instead, or GetPosition (returning a
wxPoint.)

Added wxPostEvent function that allows events to be posted and then
processed later.  This is a thread-safe way to interact with the GUI
thread from other threads.

Added Clipboard and Drag-and-Drop classes.

Added wxFontEnumerator.

Many updates to wxMenu, wxMenuBar.

wxPyEvent and wxPyCommandEvent derived classes now give you the actual
Python object in the event handler instead of a new shadow.

Added a Calendar widget from Lorne White to the library.

Made some fixes to the wxFloatbar.  It still has some troubles on
wxGTK...

Added an MVC tree control from Bryn Keller to the library.




What's new in 2.1.5
-------------------
* 12-Oct-1999

This is a quick bug-fix release to take care of a few nasties that
crept in at the last minute before 2.1.4 was called done.  No new
major features.



What's new in 2.1.4
-------------------
* 7-Oct-1999

This release is NOT synchronized with a snapshot release of wxGTK or
wxMSW.  For MSW this isn't much of a problem since you can get the
binaries from the web site.  For other platforms you'll have to build
wxGTK from CVS.  (See http://web.ukonline.co.uk/julian.smart/wxwin/cvs.htm)
To get the same set of sources from CVS that I used, checkout using
the wxPy-2-1-4 tag.

Now back to what's new...

Much more support for event-less callbacks and add-on modules.

Created add-on module with wxOGL classes.

Added wxWindow.GetChildren().  Be careful of this.  It returns a *copy*
of the list of the window's children.  While you are using the list if
anything changes in the real list (a child is deleted, etc.) then the
list you are holding will suddenly have window references to garbage
memory and your app will likely crash.  But if you are careful it works
great!

Added a bunch of new and missing methods to wxTreeCrtl.  The
SortChildren method is now supported, but currently only for the
default sort order.

Added typemaps for wxSize, wxPoint, wxRealPoint, and wxRect that allow
either the actual objects or Python sequence values to be used.  For
example, the following are equivallent::

    win = wxWindow(parent, size = wxSize(100, 100))
    win = wxWindow(parent, size = (100, 100))

Super-charged the wxHtml module.  You can now create your own tag
handlers and also have access to the parser and cell classes.  There
is a tag handler in the library at wxPython.lib.wxpTag that
understands the WXP tag and is able to place wxPython windows on HTML
pages.  See the demo for an example.

A bunch of the methods of wxMenuBar were previously ifdef'd out for
wxGTK.  Added them back in since the methods exist now.

Wrapped the wxHtmlHelpController and related classes.

Wrapped the C++ versions of wxSizer and friends.  The Python-only
versions are still in the library, but deprecated.  (You will get a
warning message if you try to use them, but the warning can be
disabled.) The usage of the C++ versions is slightly different, and
the functionality of wxBorderSizer is now part of wxBoxSizer.  I have
added a few methods to wxSizer to try and make the transition as
smooth as possible, I combined all Add methods into a single method
that handles all cases, added an AddMany method, etc.  One step I did
not take was to make the default value of flag in the Add method be
wxGROW.  This would have made it more backward compatible, but less
portable to and from wxWin C++ code.  Please see the docs and demo for
further details.

Added wxPyEvent and wxPyCommandEvent classes, derived from wxEvent and
wxCommandEvent.  Each of them has SetPyData and GetPyData methods that
accept or return a single Python object.  You can use these classes
directly or derive from them to create your own types of event objects
that can pass through the wxWindows event system without losing their
Python parts (as long as they are stored with SetPyData.)  Stay tuned
for more info and examples in future releases.

Added wxPython.lib.grids as an example of how to derive a new sizer
from the C++ sizers.  In this module you will find wxGridSizer and
wxFlexGridSizer.  wxGridSizer arrainges its items in a grid in which
all the widths and heights are the same.  wxFlexgridSizer allows
different widths and heights, and you can also specify rows and/or
columns that are growable.  See the demo for a couple examples for how
to use them.

Added the wxValidator class, and created a class named wxPyValidator
that should be used for the base class of any Python validators.  See
the demo for an example.  Please note that you MUST implement a Clone
method in your validator classes because of the way some things work
in the underlying C++ library.  I did not add wxTextValidator because
of some issues of how it transfers data to and from a wxString, which
in wxPython is automatically translated to and from Python strings, so
there would never be a concrete wxString that would hang around long
enough for the validator to do its job.  On the other hand, it should
be real easy to duplicate the functionality of wxTextValidator in a
pure Python class derived from wxPyValidator.

I've finally added a feature that has been on my list for close to two
years!  Ever wondered what that zero is for when you create your app
object?  Well now you can leave it out or explicitly set it to a true
value.  This value now controls what is to be done with sys.stdout and
sys.stderr.  A false value leaves them alone, and a true value sets
them to an instance of wxPyOnDemandOutputWindow.  (On windows the
default is true, on unix platforms the default is false.)  This class
creates a frame containing a wxTextCtrl as soon as anything is written
to sys.stdout or sys.stderr.  If you close the window it will come
back again the next time something is written.  (You can call
app.RestoreStdio to turn this off.)  If you would rather that the stdio be
redirected to a file, you can provide a second parameter to your app
object's constructor that is a filename.  If you want to use your own
class instead of wxPyOnDemandOutputWindow you can either implement
RedirectStdio() in you app class or change the value of
wxApp.outputWindowClass like this::

    class MyApp(wxApp):
        outputWindowClass = MyClass

        def OnInit(self):
            frame = MyFrame()
            self.SetTopWindow(frame)
            return true

Please see the implementation of wxPyOnDemandOutputWindow and wxApp in
wx.py for more details.  A few words of caution:  if you are running
your app in a debugger, changing sys.stdout and sys.stderr is likely
to really screw things up.

Added wxCaret.  Unfortunately it's author has still not documented it
in the wxWindows docs...

Some new 3rd party contributions in wxPython.lib.  PyShell, in
shell.py is an interesting implementation of an interactive Python
shell in wxWindows.  floatbar.py has a class derived from wxToolBar
that can sense mouse drags and then reparent itself into another
frame. Moving the new frame close to where it came from puts the tool
bar back into the original parent.  (Unfortunately there is currently
a bug in wxGTK's wxFrame.SetToolBar so the FloatBar has some
problems...)




What's new in 2.1b3
--------------------
* 1-Sep-1999

This release is synchronized with release 2.1 snapshot 9 of wxWindows.

Switched to using SWIG from CVS (see http://swig.cs.uchicago.edu/cvs.html)
for some of the new features and such.  Also they have encorporated my
patches so there is really no reason to stick with the current (very
old) release...  This version of SWIG gives the following new
features:

1. Keyword arguments.  You no longer have to specify all the
   parameters with defaults to a method just to specify a
   non-default value on the end.  You can now do this instead::

      win = wxWindow(parent, -1, style = mystyle)

2. There is now an an equivalence between Python's None and C++'s
   NULL.  This means that any methods that might return NULL will
   now return None and you can use None where wxWindows might be
   expecting NULL.  This makes things much more snake-ish.


There is a new build system based on a new Python program instead of
raw makefiles.  Now wxPython builds are virtually the same on MSW or
Unix systems.  See the end of this file for new build instructions and
see distrib/build.py for more details.

wxDC.Bilt now includes the useMask parameter, and has been split into
two different versions.  wxDC.BlitXY is like what was there before and
takes raw coordinants and sizes, and the new wxDC.Blit is for the new
interface using wxPoints and a wxSize.





What's new in 2.1b2
-------------------
* 6-Aug-1999

Added the missing wxWindow.GetUpdateRegion() method.

Made a new change in SWIG (update your patches everybody) that
provides a fix for global shadow objects that get an exception in
their __del__ when their extension module has already been deleted.
It was only a 1 line change in .../SWIG/Modules/pycpp.cxx at about
line 496 if you want to do it by hand.

It is now possible to run through MainLoop more than once in any one
process.  The cleanup that used to happen as MainLoop completed (and
prevented it from running again) has been delayed until the wxc module
is being unloaded by Python.

I fixed a bunch of stuff in the C++ version of wxGrid so it wouldn't
make wxPython look bad.

wxWindow.PopupMenu() now takes a wxPoint instead of  x,y.  Added
wxWindow.PopupMenuXY to be consistent with some other methods.

Added wxGrid.SetEditInPlace and wxGrid.GetEditInPlace.

You can now provide your own app.MainLoop method.  See
wxPython/demo/demoMainLoop.py for an example and some explanation.

Got the in-place-edit for the wxTreeCtrl fixed and added some demo
code to show how to use it.

Put the wxIcon constructor back in for GTK as it now has one that
matches MSW's.

Added wxGrid.GetCells

Added wxSystemSettings static methods as functions with names like
wxSystemSettings_GetSystemColour.

Removed wxPyMenu since using menu callbacks have been deprecated in
wxWindows.  Use wxMenu and events instead.

Added alternate wxBitmap constructor (for MSW only) as
      wxBitmapFromData(data, type, width, height, depth = 1)

Added a helper function named wxPyTypeCast that can convert shadow
objects of one type into shadow objects of another type.  (Like doing
a down-cast.)  See the implementation in wx.py for some docs.

Fixed wxImage GetData and SetData to properly use String objects for
data transfer.

Added access methods to wxGridEvent.

New Makefile/Setup files supporting multiple dynamic extension modules
for unix systems.

Fixes for the wxGLCanvas demo to work around a strange bug in gtk.

SWIG support routines now compiled separately instead of being bundled
in wx.cpp.





What's new in 2.1b1
-------------------
* 28-Jun-1999

Fixed wxComboBox.SetSelection so that it actually sets the selected
item.  (Actually just removed it from wxPython and let it default to
wxChoice.SetSelection which was already doing the right thing.)

Added the Printing Framework.

Switched back to using the wxWindows DLL for the pre-built Win32
version.  The problem was needing to reinitialize static class info
data after loading each extension module.

Lots of little tweaks and additions to reflect changes to various
wxWindows classes.

Fixed a bug with attaching objects to tree items.  Actually was a
symptom of a larger problem with not obtaining the interpreter lock
when doing any Py_DECREFs.

wxSizer and friends.  Sizers are layout tools that manage a collection
of windows and sizers.  Different types of sizers apply different
types of layout algorithms.  You saw it here first!  These classes are
not even in the wxWindows C++ library yet!



What's new in 2.0b9
-------------------
* 1-May-1999

Bug fix for ListCtrl in test4.py (Was a missing file...  DSM!)

Bug fix for occasional GPF on Win32 systems upon termination of a
wxPython application.

Added wxListBox.GetSelections returning selections as a Tuple.

Added a wxTreeItemData that is able to hold any Python object and be
associated with items in a wxTreeCtrl.  Added test pytree.py to show
this feature off.

Added wxSafeYield function.

OpenGL Canvas can be optionally compiled in to wxPython.

Awesome new Demo Framework for showing off wxPython and for learning
how it all works.

The pre-built Win32 version is no longer distributing the wxWindows
DLL.  It is statically linked with the wxWindows library instead.

Added a couple missing items from the docs.

Added wxImage, wxImageHandler, wxPNGHandler, wxJPEGHandler,
wxGIFHandler and wxBMPHandler.

Added new methods to wxTextCtrl.

Fixed some problems with how SWIG was wrapping some wxTreeCtrl
methods.



What's new in 2.0b8
-------------------
* 28-Mar-1999

Support for using Python threads in wxPython apps.

Several missing methods from various classes.

Various bug fixes.



What's new in 2.0b7
-------------------
* 15-Mar-1999

Added DLG_PNT and DLG_SZE convenience methods to wxWindow class.

Added missing constructor and other methods for wxMenuItem.



What's new in 2.0b6
-------------------
* 4-Mar-1999

Just a quickie update to fix the self-installer to be compatible with
Python 1.5.2b2's Registry settings.


What's new in 2.0b5
-------------------
* 25-Feb-1999

Well obviously the numbering scheme has changed.  I did this to
reflect the fact that this truly is the second major revision of
wxPython, (well the third actually if you count the one I did for
wxWindows 1.68 and then threw away...) and also that it is associated
with the 2.0 version of wxWindows.

I have finally started documenting wxPython.  There are several pages
in the wxWindows documentation tree specifically about wxPython, and I
have added notes within the class references about where and how wxPython
diverges from wxWindows.

Added wxWindow_FromHWND(hWnd) for wxMSW to construct a wxWindow from a
window handle.  If you can get the window handle into the python code,
it should just work...  More news on this later.

Added wxImageList, wxToolTip.

Re-enabled wxConfig.DeleteAll() since it is reportedly fixed for the
wxRegConfig class.

As usual, some bug fixes, tweaks, etc.



What's new in 0.5.3
-------------------
* 30-Jan-1999

Added wxSashWindow, wxSashEvent, wxLayoutAlgorithm, etc.

Various cleanup, tweaks, minor additions, etc. to maintain
compatibility with the current wxWindows.



What's new in 0.5.0
-------------------
Changed the import semantics from ``"from wxPython import *"`` to
``"from wxPython.wx import *"``  This is for people who are worried about
namespace pollution, they can use "from wxPython import wx" and then
prefix all the wxPython identifiers with "wx."

Added wxTaskbarIcon for wxMSW.

Made the events work for wxGrid.

Added wxConfig.

Added wxMiniFrame for wxGTK.

Changed many of the args and return values that were pointers to gdi
objects to references to reflect changes in the wxWindows API.

Other assorted fixes and additions.




What's new in 0.4.2
-------------------
* 21-Oct-1998

wxPython on wxGTK works!!!  Both dynamic and static on Linux and
static on Solaris have been tested.  Many thanks go to Harm van der
Heijden for his astute detective work on tracking down a nasty DECREF
bug.  Okay so I have to confess that it was just a DSM (Dumb Stupid
Mistake) on my part but it was nasty none the less because the
behavior was so different on different platforms.

The dynamically loaded module on Solaris is still segfaulting, so it
must have been a different issue all along...



What's New in 0.4
-----------------
* 2-Oct-1998

1. Worked on wxGTK compatibility.  It is partially working.  On a
Solaris/Sparc box wxPython is working but only when it is statically
linked with the Python interpreter.  When built as a dynamically loaded
extension module, things start acting weirdly and it soon seg-faults.
And on Linux both the statically linked and the dynamically linked
version segfault shortly after starting up.

2. Added Toolbar, StatusBar and SplitterWindow classes.

3. Various bug fixes, enhancements, etc.




wxPython 0.3
------------
* 9-Aug-1998

The first "modern" version of wxPython.  See https://wxpython.org/pages/history/


.. -*- coding: utf-8 -*-
