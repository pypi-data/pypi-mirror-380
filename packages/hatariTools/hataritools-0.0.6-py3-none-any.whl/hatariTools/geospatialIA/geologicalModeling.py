import os
import vtk
import numpy as np
import pandas as pd
import pyvista as pv
import seaborn as sns
import matplotlib.pyplot as plt

import fiona
import rasterio
from rasterio.plot import show
import geopandas as gpd
from shapely.geometry import Polygon, Point

from skimage.feature import match_template
from mpl_toolkits.axes_grid1 import make_axes_locatable
from skimage.feature import match_template
from sklearn.cluster import Birch

from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

from hatariTools.utils import (isRunningInJupyter, 
                    printBannerHtml, 
                    printBannerText)

class geoModel():
    def __init__(self):
        self.fileDict = {}
        self.locDict = {}
        self.litoDict = {}
        self.litoFileDict = {}

        #insert banner
        if isRunningInJupyter():
            printBannerHtml()
        else:
            printBannerText()

        print('\n/-------------------------------------------/')
        print('\nThe geological modeling engine has been started')
        print('\n/-------------------------------------------/')

    fileDictReqFields = ['locationFile','litoFile','outputDir']
    locDictReqFields = ['id','easting','northing','elevation']
    litoFileDictReqFields = ['id','top','bottom','litoCode']

    def hasRequiredFields(self, dataDict, requiredFields):
        return all(field in dataDict for field in requiredFields)
    
    def defineFileDict(self, fileDict):
        if self.hasRequiredFields(fileDict, self.fileDictReqFields):
            self.fileDict = fileDict
            print("The file dictionary has been added.")
        else: 
            print("The provided dictionary doesn't have one of the \
                  following keys:", ", ".join(f"{item}%" for item in self.fileDictReqFields))

    def defineLitoDict(self, litoDict):
        self.litoDict = litoDict
        print("The lithology dictionary has been added.")

    def defineLocDict(self, locDict):
        if self.hasRequiredFields(locDict, self.locDictReqFields):
            self.locDict = locDict
            print("The location header dictionary has been added.")
        else: 
            print("The provided dictionary doesn't have one of the \
                  following keys:", ", ".join(f"{item}%" for item in self.locDictReqFields))
            
    def defineLitoFileDict(self, litoFileDict):
        if self.hasRequiredFields(litoFileDict, self.litoFileDictReqFields):
            self.litoFileDict = litoFileDict
            print("The lithology header dictionary has been added.")
        else: 
            print("The provided dictionary doesn't have one of the \
                  following keys:", ", ".join(f"{item}%" for item in self.litoFileDictReqFields))
            
    def generatePointCloud(self, resolution=0.3):
        #import well location
        wellLoc = pd.read_csv(self.fileDict['locationFile'])
        wellLoc = wellLoc.set_index(self.locDict['id'])

        #import borehole litology
        wellLito = pd.read_csv(self.fileDict['litoFile'])

        #create empty columns
        wellLito['elevTop'] = -10000
        wellLito['elevBot'] = -10000

        for index, row in wellLito.iterrows():
            #print(row)
            try:
                surfElev = wellLoc.loc[row[self.litoFileDict['id']],self.locDict['elevation']]
                wellLito.loc[index,'elevTop'] = surfElev - row[self.litoFileDict['top']]
                wellLito.loc[index,'elevBot'] = surfElev - row[self.litoFileDict['bottom']]
            except KeyError:
                wellLito = wellLito.drop(index)

        #check well lito and export as csv
        litoName = self.fileDict['locationFile'].split('.')[0]
        # litoElevFile = os.path.join(self.fileDict['outputDir'],litoName+'_Elev.csv')
        # wellLito.to_csv(litoElevFile)
        # self.fileDict['litoElevFile'] = litoElevFile

        #store dataframes for later use
        self.wellLitoDf = wellLito
        self.wellLocDf = wellLoc

        litoPoints = []

        for index, values in self.wellLitoDf.iterrows():
            id = self.locDict['id']
            easting = self.locDict['easting']
            northing = self.locDict['northing']
            elevation = self.locDict['elevation']
            wellX, wellY, wellZ = self.wellLocDf.loc[values[self.litoFileDict['id']]][[easting,northing,elevation]]
            wellXY = [wellX, wellY]
            litoPoints.append(wellXY + [values.elevTop,values[self.litoFileDict['litoCode']]])
            litoPoints.append(wellXY + [values.elevBot,values[self.litoFileDict['litoCode']]])

            litoLength = values.elevTop - values.elevBot
            
            depthResolution = resolution
            if litoLength < depthResolution:
                midPoint = wellXY + [values.elevTop - litoLength/2,values[self.litoFileDict['litoCode']]]
            else:
                npoints = int(litoLength/depthResolution)
                for point in range(1,npoints):
                    disPoint = wellXY + [values.elevTop - litoLength*point/npoints,values[self.litoFileDict['litoCode']]]
                    litoPoints.append(disPoint)
        self.litoPointCloud=np.array(litoPoints)
        pointCloudFile = os.path.join(self.fileDict['outputDir'],'litoPointCloud')
        np.save(pointCloudFile,self.litoPointCloud)

    def generateLitoRepresentation(self):
        #generation of list arrays for the vtk
        offsetList = []
        linSec = []
        linVerts = []

        i=0
        for index, values in self.wellLitoDf.iterrows():
            x, y = self.wellLocDf.loc[values[self.locDict['id']]][[self.locDict['easting'],self.locDict['northing']]]
            cellVerts = [[x,y,values.elevTop],[x,y,values.elevBot]] # no van estos terminos :[self.litoFileDict['top'],[self.litoFileDict['bottom']
            #print(cellVerts)
            offsetList.append(i*3)         
            linSec = linSec + [2,2*i,2*i+1]
            linVerts = linVerts + cellVerts
            i +=1

        offsetArray = np.array(offsetList)
        linArray = np.array(linSec)
        cellType = np.ones([i])*3
        vertArray = np.array(linVerts)
        # create the unstructured grid and assign lito code
        grid = pv.UnstructuredGrid(linArray, cellType, vertArray)
        grid.cell_data["values"] = self.wellLitoDf[self.litoFileDict['litoCode']].values
        litoVtuFile = os.path.join(self.fileDict['outputDir'],'conceptualizedLito.vtu')
        grid.save(litoVtuFile,binary=False)

    # Point cloud of lithologies

    # def generatePointCloud(self, resolution=0.3):

    #     litoPoints = []

    #     for index, values in self.wellLitoDf.iterrows():
    #         id = self.locDict['id']
    #         easting = self.locDict['easting']
    #         northing = self.locDict['northing']
    #         elevation = self.locDict['elevation']
    #         wellX, wellY, wellZ = self.wellLocDf.loc[values.id][[easting,northing,elevation]]
    #         wellXY = [wellX, wellY]
    #         litoPoints.append(wellXY + [values.elevTop,values[self.litoFileDict['litoCode']]])
    #         litoPoints.append(wellXY + [values.elevBot,values[self.litoFileDict['litoCode']]])

    #         litoLength = values.elevTop - values.elevBot
            
    #         depthResolution = resolution
    #         if litoLength < depthResolution:
    #             midPoint = wellXY + [values.elevTop - litoLength/2,values.litoCode]
    #         else:
    #             npoints = int(litoLength/depthResolution)
    #             for point in range(1,npoints):
    #                 disPoint = wellXY + [values.elevTop - litoLength*point/npoints,values.litoCode]
    #                 litoPoints.append(disPoint)
    #     self.litoPointCloud=np.array(litoPoints)
    #     pointCloudFile = os.path.join(self.fileDict['outputDir'],'litoPointCloud')
    #     np.save(pointCloudFile,self.litoPointCloud)

# Coordinate transformation and Neural Network Classifier setup
    def buildNeuralClassifier(self):
        #transform to local coordinates
        litoX, litoY, litoZ = self.litoPointCloud[:,0], self.litoPointCloud[:,1], self.litoPointCloud[:,2]
        self.litoMean = self.litoPointCloud[:,:3].mean(axis=0)
        self.litoTrans = self.litoPointCloud[:,:3]-self.litoMean
        #print(litoTrans[0:150:30])

        #setting up scaler
        self.scaler = preprocessing.StandardScaler().fit(self.litoTrans)
        litoScale = self.scaler.transform(self.litoTrans)

        #check scaler
        #print(litoScale.mean(axis=0))
        #print(litoScale.std(axis=0))

        #define x and y
        X = litoScale
        y = self.litoPointCloud[:,3]

        #split in train and test
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

        #run classifier
        self.clf = MLPClassifier(activation='tanh',
                                 solver='lbfgs',
                                 hidden_layer_sizes=(15,15,15,15,15),
                                 alpha=0.0001, 
                                 max_iter=3000)
        self.clf.fit(X_train,y_train)

        numberSamples = X_test.shape[0]
        expected=y_test
        predicted = []
        for i in range(numberSamples):
            predicted.append(self.clf.predict([X_test[i]]))
        results = confusion_matrix(expected,predicted)

        # Apply color gradient to DataFrame in terminal or notebook display
        litoDf = pd.DataFrame(self.litoDict, index=[1])
        #print(litoDf)

        # Plot the matrix as a heatmap
        sns.heatmap(results, 
                    annot=True, 
                    fmt="d",
                    cmap="coolwarm", 
                    linecolor='white', 
                    yticklabels=litoDf.columns.values.tolist(),
                    xticklabels=litoDf.columns.values.tolist(),
                    linewidths=1)
        plt.show()



    def generatePredictedGrid(self, cellHeight=0.3, cellWidth=20):

        # Area of study and output grid refinement
        xMin = self.wellLocDf[self.locDict['easting']].min()//100*100
        xMax = self.wellLocDf[self.locDict['easting']].max()//100*100
        #print(xMax-xMin)
        yMin = self.wellLocDf[self.locDict['northing']].min()//100*100
        yMax = self.wellLocDf[self.locDict['northing']].max()//100*100
        #print(yMax-yMin)
        zMax = round(self.wellLitoDf['elevTop'].max(),1)
        zMin = round(self.wellLitoDf['elevBot'].min(),1)
        #print(zMax-zMin)

        #definition of output cell size
        cellH = cellWidth
        cellV = cellHeight

        #create arrangement of vertex and cells
        vertexCols = np.arange(xMin,xMax+cellH,cellH)
        vertexRows = np.arange(yMax,yMin-cellH,-cellH)
        vertexLays = np.arange(zMax,zMin-cellV,-cellV)
        cellCols = (vertexCols[1:]+vertexCols[:-1])/2
        cellRows = (vertexRows[1:]+vertexRows[:-1])/2 
        cellLays = (vertexLays[1:]+vertexLays[:-1])/2
        nCols = cellCols.shape[0]
        nRows = cellRows.shape[0]
        nLays = cellLays.shape[0]
        print('/---------- size of predicted grid ----------/')
        print("Cols: %d, Rows: %d, Lays: %d"%(nCols,nRows,nLays))

        i=0
        litoMatrix=np.zeros([nLays,nRows,nCols])
        for lay in range(nLays):
            for row in range(nRows):
                for col in range(nCols):
                    cellXYZ = [cellCols[col],cellRows[row],cellLays[lay]]
                    cellTrans = cellXYZ - self.litoMean
                    cellNorm = self.scaler.transform([cellTrans])
                    
                    litoMatrix[lay,row,col] = self.clf.predict(cellNorm)
                    
                    if i%100000==0:
                        print("Processing %s cells"%i)
                        # print(cellTrans)
                        # print(cellNorm)
                        # print(litoMatrix[lay,row,col])
                    i+=1
        print('/---------- plot sample layer ----------/')
        plt.imshow(litoMatrix[10])

        self.litoMatrixMod = litoMatrix[::-1,::-1,::-1]

        # Create empty grid
        grid = pv.RectilinearGrid()

        # Initialize from a vtk.vtkRectilinearGrid object
        vtkgrid = vtk.vtkRectilinearGrid()
        grid = pv.RectilinearGrid(vtkgrid)
        grid = pv.RectilinearGrid(vertexCols,vertexRows,vertexLays)

        litoFlat = list(self.litoMatrixMod.flatten(order="K"))[::-1]
        grid.cell_data["geoCode"] = np.array(litoFlat)
        gridVtuFile = os.path.join(self.fileDict['outputDir'],'predictedGeology.vtk')
        grid.save(gridVtuFile)



