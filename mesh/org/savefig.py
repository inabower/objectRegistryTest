# state file generated using paraview version 5.9.0-RC3

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [1079, 770]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [0.25, 0.0, 0.004999999888241291]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [0.25, 0.0, 0.9902443432590722]
renderView1.CameraFocalPoint = [0.25, 0.0, 0.004999999888241291]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 0.2550000001438985

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)
layout1.SetSize(1079, 770)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'OpenFOAMReader'
oilFlow_0foam = OpenFOAMReader(registrationName='oilFlow_0.foam', FileName='/mnt/c/work/simulation/storeIO/results/oilFlow_0/oilFlow_0.foam')
oilFlow_0foam.MeshRegions = ['internalMesh']
oilFlow_0foam.CellArrays = ['U', 'alpha.water', 'massInlet', 'p', 'p_rgh', 's']

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=oilFlow_0foam)
calculator1.ResultArrayName = 'salpha'
calculator1.Function = '(1.0-alpha.water)+s*10'

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from calculator1
calculator1Display = Show(calculator1, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'salpha'
salphaLUT = GetColorTransferFunction('salpha')
salphaLUT.AutomaticRescaleRangeMode = 'Never'
#salphaLUT.RGBPoints = [0.0, 0.0, 0.0, 0.0, 0.666, 0.0, 0.0, 0.501960784314, 1.332, 0.0, 0.501960784314, 1.0, 2.0, 1.0, 1.0, 1.0]
salphaLUT.RGBPoints = [
      0.00000, 0.00000, 0.00000, 0.00000,
      0.04000, 0.90196, 0.00000, 0.00000,
      0.08000, 0.90196, 0.90196, 0.00000,
      0.10000, 1.00000, 1.00000, 1.00000,
      0.12000, 0.90196, 0.90196, 0.00000,
      0.16000, 0.90196, 0.00000, 0.00000,
      0.20000, 0.00000, 0.00000, 0.00000,
      0.24000, 0.90196, 0.00000, 0.00000,
      0.28000, 0.90196, 0.90196, 0.00000,
      0.30000, 1.00000, 1.00000, 1.00000,
      0.32000, 0.90196, 0.90196, 0.00000,
      0.36000, 0.90196, 0.00000, 0.00000,
      0.40000, 0.00000, 0.00000, 0.00000,
      0.44000, 0.90196, 0.00000, 0.00000,
      0.48000, 0.90196, 0.90196, 0.00000,
      0.50000, 1.00000, 1.00000, 1.00000,
      0.52000, 0.90196, 0.90196, 0.00000,
      0.56000, 0.90196, 0.00000, 0.00000,
      0.60000, 0.00000, 0.00000, 0.00000,
      0.64000, 0.90196, 0.00000, 0.00000,
      0.68000, 0.90196, 0.90196, 0.00000,
      0.70000, 1.00000, 1.00000, 1.00000,
      0.72000, 0.90196, 0.90196, 0.00000,
      0.76000, 0.90196, 0.00000, 0.00000,
      0.80000, 0.00000, 0.00000, 0.00000,
      0.84000, 0.90196, 0.00000, 0.00000,
      0.88000, 0.90196, 0.90196, 0.00000,
      0.90000, 1.00000, 1.00000, 1.00000,
      0.92000, 0.90196, 0.90196, 0.00000,
      0.96000, 0.90196, 0.00000, 0.00000,
      1.00000, 1.00000, 1.00000, 1.00000,
      1.00000, 0.00000, 0.00000, 0.00000,
      1.03330, 0.00000, 0.00000, 0.50196,
      1.06660, 0.00000, 0.50196, 1.00000,
      1.10000, 1.00000, 1.00000, 1.00000,
      1.13340, 0.00000, 0.50196, 1.00000,
      1.16670, 0.00000, 0.00000, 0.50196,
      1.20000, 0.00000, 0.00000, 0.00000,
      1.23330, 0.00000, 0.00000, 0.50196,
      1.26660, 0.00000, 0.50196, 1.00000,
      1.30000, 1.00000, 1.00000, 1.00000,
      1.33340, 0.00000, 0.50196, 1.00000,
      1.36670, 0.00000, 0.00000, 0.50196,
      1.40000, 0.00000, 0.00000, 0.00000,
      1.43330, 0.00000, 0.00000, 0.50196,
      1.46660, 0.00000, 0.50196, 1.00000,
      1.50000, 1.00000, 1.00000, 1.00000,
      1.53340, 0.00000, 0.50196, 1.00000,
      1.56670, 0.00000, 0.00000, 0.50196,
      1.60000, 0.00000, 0.00000, 0.00000,
      1.63330, 0.00000, 0.00000, 0.50196,
      1.66660, 0.00000, 0.50196, 1.00000,
      1.70000, 1.00000, 1.00000, 1.00000,
      1.73340, 0.00000, 0.50196, 1.00000,
      1.76670, 0.00000, 0.00000, 0.50196,
      1.80000, 0.00000, 0.00000, 0.00000,
      1.83330, 0.00000, 0.00000, 0.50196,
      1.86660, 0.00000, 0.50196, 1.00000,
      1.90000, 1.00000, 1.00000, 1.00000,
      1.93340, 0.00000, 0.50196, 1.00000,
      1.96670, 0.00000, 0.00000, 0.50196,
      2.00000, 1.00000, 1.00000, 1.00000]
salphaLUT.ColorSpace = 'RGB'
salphaLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'salpha'
salphaPWF = GetOpacityTransferFunction('salpha')
salphaPWF.Points = [0.0, 0.0, 0.5, 0.0, 2.0, 1.0, 0.5, 0.0]
salphaPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
calculator1Display.Representation = 'Surface'
calculator1Display.ColorArrayName = ['POINTS', 'salpha']
calculator1Display.LookupTable = salphaLUT
calculator1Display.SelectTCoordArray = 'None'
calculator1Display.SelectNormalArray = 'None'
calculator1Display.SelectTangentArray = 'None'
calculator1Display.OSPRayScaleArray = 'p'
calculator1Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator1Display.SelectOrientationVectors = 'U'
calculator1Display.ScaleFactor = 0.05
calculator1Display.SelectScaleArray = 'p'
calculator1Display.GlyphType = 'Arrow'
calculator1Display.GlyphTableIndexArray = 'p'
calculator1Display.GaussianRadius = 0.0025
calculator1Display.SetScaleArray = ['POINTS', 'p']
calculator1Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator1Display.OpacityArray = ['POINTS', 'p']
calculator1Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator1Display.DataAxesGrid = 'GridAxesRepresentation'
calculator1Display.PolarAxes = 'PolarAxesRepresentation'
calculator1Display.ScalarOpacityFunction = salphaPWF
calculator1Display.ScalarOpacityUnitDistance = 0.051000000028779705
calculator1Display.OpacityArrayName = ['POINTS', 'p']
calculator1Display.ExtractedBlockIndex = 1

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator1Display.ScaleTransferFunction.Points = [-388.9855041503906, 0.0, 0.5, 0.0, 530.7879638671875, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator1Display.OpacityTransferFunction.Points = [-388.9855041503906, 0.0, 0.5, 0.0, 530.7879638671875, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for salphaLUT in view renderView1
salphaLUTColorBar = GetScalarBar(salphaLUT, renderView1)
salphaLUTColorBar.Title = 'salpha'
salphaLUTColorBar.ComponentTitle = ''

# set color bar visibility
salphaLUTColorBar.Visibility = 1

# show color legend
calculator1Display.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# restore active source
SetActiveSource(calculator1)
# ----------------------------------------------------------------

calculator1Display.SetScalarBarVisibility(renderView1, False)
renderView1.OrientationAxesVisibility = 0
renderView1.CameraPosition = [0.25, 0.0, 0.5]
renderView1.CameraFocalPoint = [0.25, 0.0, 0.0]
renderView1.CameraParallelScale = 0.2

n = 0
for t in oilFlow_0foam.TimestepValues:
	renderView1.ViewTime = t
	fileName = 'pic/flow_{:04d}.png'.format(n)
	SaveScreenshot(fileName, renderView1, ImageResolution=(960,480))
	n += 1

if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')