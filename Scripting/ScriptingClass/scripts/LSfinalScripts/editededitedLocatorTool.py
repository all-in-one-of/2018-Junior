import maya.cmds as cmds

class LocatorWindow():
    def __init__(self):
        self.mWin = 'LocWindow'

    def create(self):
        self.delete()

        self.mWin = cmds.window(self.mWin, title='Create Locator')
        mCol = cmds.columnLayout(parent=self.mWin, adjustableColumn=True)
        self.dropCtrl = cmds.optionMenu(parent=mCol, label='Type')
        cmds.menuItem(parent=self.dropCtrl, label='Bounding Box')
        cmds.menuItem(parent=self.dropCtrl, label='Pivot Point')
        cmds.button(parent=mCol, label='Create Locator',
                    c=lambda x: self.create_loc_window(cmds.optionMenu(self.dropCtrl, q=True, select=True)))

        cmds.showWindow(self.mWin)

    def delete(self):
        if cmds.window(self.mWin, exists=True):
            cmds.deleteUI(self.mWin)

    def create_loc_window(self, option):
        '''Creates a locator at center of selection or pivot based on input.'''
        sels = cmds.ls(sl=True)

        # create locator at center of selections
        if option is 1:

            bbox = cmds.exactWorldBoundingBox(sels)
            pivot = [(bbox[0] + bbox[3]) / 2, (bbox[1] + bbox[4]) / 2, (bbox[2] + bbox[5]) / 2]

            loc = cmds.spaceLocator()[0]
            cmds.xform(loc, translation=pivot, worldSpace=True)

        # create locator at pivot point of each selection
        elif option is 2:
            for sel in sels:
                pivot = cmds.xform(sel, q=True, rp=True, ws=True)
                loc = cmds.spaceLocator()[0]
                cmds.xform(loc, translation=pivot, worldSpace=True)

        cmds.showWindow(self.mWin)

var = LocatorWindow()
var.create()