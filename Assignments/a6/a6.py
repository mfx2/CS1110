# a6.py
# Michael Xiao - mfx2; and Debo Adebola - aaa292
# November 13, 2016
"""Classes to perform KMeans Clustering"""

import math
import random
import numpy
import copy

# HELPER FUNCTIONS FOR ASSERTS GO HERE
def is_point(thelist):
    """Return: True if thelist is a list of int or float"""
    if (type(thelist) != list):
        return False
    
    # All float
    okay = True
    for x in thelist:
        if (not type(x) in [int,float]):
            okay = False
    
    return okay


# CLASSES
class Dataset(object):
    """Instance is a dataset for k-means clustering.
    
    The data is stored as a list of list of numbers
    (ints or floats).  Each component list is a data point.
    
    Instance Attributes:
        _dimension: the point dimension for this dataset
            [int > 0. Value never changes after initialization]
        
        _contents: the dataset contents
            [a 2D list of numbers (float or int), possibly empty]:
    
    ADDITIONAL INVARIANT:
        The number of columns in _contents is equal to _dimension.  
        That is, for every item _contents[i] in the list _contents, 
        len(_contents[i]) == dimension.
    
    None of the attributes should be accessed directly outside of the class
    Dataset (e.g. in the methods of class Cluster or KMeans). Instead, this class 
    has getter and setter style methods (with the appropriate preconditions) for 
    modifying these values.
    """
    
    def __init__(self, dim, contents=None):
        """Initializer: Creates a dataset for the given point dimension.
        
        Note that contents (which is the initial value for attribute _contents)
        is optional. When assigning contents to the attribute _contents the initializer
        COPIES the  list contents. If contents is None, the initializer assigns 
        _contents an empty list.
        
        Parameter dim: the initial value for attribute _dimension.  
        Precondition: dim is an int > 0.
        
        Parameter contents: the initial value for attribute _contents (optional). 
        Precondition: contents is either None or is a 2D list of numbers (int or float). 
        If contents is not None, then contents if not empty and the number of columns of 
        contents is equal to dim.
        """
        assert type(dim) == int and dim>0
        assert contents == None or contents != None
        if contents != None:
            for x in contents:
               assert is_point(x) == True
               assert len(x) == dim
               
        self._dimension = dim
                    
        if contents == None:
            self._contents = []
        else:
            self._contents = copy.deepcopy(contents)
    
    def getDimension(self):
        """Returns: The point dimension of this data set.
        """
        return self._dimension
    
    def getSize(self):
        """Returns: the number of elements in this data set.
        """
        return len(self._contents)
    
    def getContents(self):
        """Returns: The contents of this data set as a list.
        
        This method returns the attribute _contents directly.  Any changes made to this 
        list will modify the data set.  If you want to access the data set, but want to 
        protect yourself from modifying the data, use getPoint() instead.
        """
        return self._contents
    
    def getPoint(self, i):
        """Returns: A COPY of the point at index i in this data set.
        
        Often, we want to access a point in the data set, but we want a copy
        to make sure that we do not accidentally modify the data set.  That
        is the purpose of this method.  
        
        If you actually want to modify the data set, use the method getContents().
        That returns the list storing the data set, and any changes to that
        list will alter the data set.
        
        Parameter i: the index position of the point
        Precondition: i is an int that refers to a valid position in 0..getSize()-1
        """
        assert type(i) == int and i >= 0 and i <= (self.getSize()-1)
        
        return copy.deepcopy(self._contents[i])
    
    def addPoint(self,point):
        """Adds a COPY of point at the end of _contents.
        
        This method does not add the point directly. It adds a copy of the point.
        
        Parameter point: the point to add
        Precondition: point is a list of numbers (int or float), len(point) = _dimension.
        """
        assert is_point(point) == True
        assert len(point) == self._dimension
        
        a = copy.deepcopy(point)
        self._contents.append(a)
        
    # PROVIDED METHODS: Do not modify!
    def __str__(self):
        """Returns: String representation of the centroid of this cluster."""
        return str(self._contents)
    
    def __repr__(self):
        """Returns: Unambiguous representation of this cluster. """
        return str(self.__class__) + str(self)


class Cluster(object):
    """An instance is a cluster, a subset of the points in a dataset.
    
    A cluster is represented as a list of integers that give the indices
    in the dataset of the points contained in the cluster.  For instance,
    a cluster consisting of the points with indices 0, 4, and 5 in the
    dataset's data array would be represented by the index list [0,4,5].
    
    A cluster instance also contains a centroid that is used as part of
    the k-means algorithm.  This centroid is an n-D point (where n is
    the dimension of the dataset), represented as a list of n numbers,
    not as an index into the dataset.  (This is because the centroid
    is generally not a point in the dataset, but rather is usually in between
    the data points.)
    
    Instance Attributes:
        _dataset: the dataset this cluster is a subset of  [Dataset]
        
        _indices: the indices of this cluster's points in the dataset  [list of int]
        
        _centroid: the centroid of this cluster  [list of numbers]
    
    ADDITIONAL INVARIANTS:
        len(_centroid) == _dataset.getDimension()
        0 <= _indices[i] < _dataset.getSize(), for all 0 <= i < len(_indices)
    """
    
    # Part A
    def __init__(self, ds, centroid):
        """Initializer: Creates a new empty cluster with the given centroid.
        
        Remember that a centroid is a point and hence a list.  The initializer COPIES
        the centroid; it does not use the original list.
        
        IMPORTANT: READ THE PRECONDITION OF ds VERY CAREFULLY
        
        Parameter ds: the Dataset for this cluster
        Precondition: ds is a instance of Dataset OR a subclass of Dataset
        
        Parameter centroid: the centroid point (which might not be a point in ds)
        Precondition: centroid is a list of numbers (int or float),
          len(centroid) = ds.getDimension()
        """
        assert isinstance(ds, Dataset)
        assert is_point(centroid) and len(centroid) == ds.getDimension()
        
        self._dataset = ds
        self._centroid = centroid
        self._indices = []
        
    def getCentroid(self):
        """Returns: the centroid of this cluster.
        
        This getter method is to protect access to the centroid.
        """
        return copy.deepcopy(self._centroid)
    
    def getIndices(self):
        """Returns: the indices of points in this cluster
        
        This method returns the attribute _indices directly.  Any changes
        made to this list will modify the cluster.
        """
        return copy.deepcopy(self._indices)
    
    def addIndex(self, index):
        """Adds the given dataset index to this cluster.
        
        If the index is already in this cluster, then this method leaves the
        cluster unchanged.
        
        Parameter index: the index of the point to add
        Precondition: index is a valid index into this cluster's dataset.
        That is, index is an int in the range 0.._dataset.getSize()-1.
        """
        
        assert type(index) == int
        assert index >= 0 and index <= self._dataset.getSize()
        
        if index in self.getIndices():
            pass
        else:
            self._indices.append(index)
    
    def clear(self):
        """Removes all points from this cluster, but leave the centroid unchanged.
        """
        self._indices = []
    
    def getContents(self):
        """Returns: a new list containing copies of the points in this cluster.
        
        The result is a list of list of numbers.  It has to be computed from
        the indices.
        """
        copy = []
        for i in range(len(self.getIndices())):
            copy.append(self._dataset.getPoint(self.getIndices()[i]))
        return copy
    
    # Part B
    def distance(self, point):
        """Returns: The euclidean distance from point to this cluster's centroid.
        
        Parameter point: the point to compare to this cluster's centroid
        Precondition: point is a list of numbers (int or float),
          len(point) = _ds.getDimension()
        """
        assert len(point) == self._dataset.getDimension()
        a = self.getCentroid()
        square = 0
        for x in range(len(point)):
            square = square + (float(point[x]) - float(self.getCentroid()[x]))**2 
            
        return math.sqrt(square)
    
    def updateCentroid(self):
        """Returns: Trues if the centroid remains unchanged; False otherwise.
        
        This method recomputes the _centroid attribute of this cluster. The
        new _centroid attribute is the average of the points of _contents
        (To average a point, average each coordinate separately).  
        
        Whether the centroid "remained the same" after recomputation is determined 
        by the function numpy.allclose().  The return value should be interpreted
        as an indication of whether the starting centroid was a "stable" position 
        or not.
        
        If there are no points in the cluster, the centroid. does not change.
        """
        old  = self._centroid
        sum = [0 for x in range(self._dataset.getDimension())]
        
        if self.getContents() == []:
            new = self._centroid
        else:
            for i in self.getContents():
                for j in range(len(i)):
                    sum[j] = sum[j] + i[j]
        
        new = [sum[j]/len(self.getContents()) for j in range(len(sum))]            
        
        self._centroid = new
        
        return numpy.allclose(old,new)
    
    # PROVIDED METHODS: Do not modify!
    def __str__(self):
        """Returns: String representation of the centroid of this cluster."""
        return str(self._centroid)
    
    def __repr__(self):
        """Returns: Unambiguous representation of this cluster. """
        return str(self.__class__) + str(self)


class ClusterGroup(object):
    """An instance is a set of clusters of the points in a dataset.
    
    Instance Attributes:
        _dataset: the dataset which this is a clustering of     [Dataset]
        
        _clusters: the clusters in this clustering (not empty)  [list of Cluster]
    """
    
    # Part A
    def __init__(self, ds, k, seed_inds=None):
        """Initializer: Creates a clustering of the dataset ds into k clusters.
        
        The clusters are initialized by randomly selecting k different points
        from the database to be the centroids of the clusters.  If seed_inds
        is supplied, it is a list of indices into the dataset that specifies
        which points should be the initial cluster centroids.
        
        IMPORTANT: READ THE PRECONDITION OF ds VERY CAREFULLY
        
        Parameter ds: the Dataset for this cluster group
        Precondition: ds is a instance of Dataset OR a subclass of Dataset
        
        Parameter k: The number of clusters (the k in k-means)
        Precondition: k is an int, 0 < k <= ds.getSize()
        
        Parameter seed_inds: the INDEXES of the points to start with
        Precondition: seed_inds is None, or a list of k valid indices into ds.
        """
        assert isinstance(ds, Dataset)
        assert type(k)==int and k>0 and k<=ds.getSize()
        assert seed_inds is None or (type(seed_inds)==list and len(seed_inds)==k)
        if seed_inds != None:
            for x in seed_inds:
                assert type(x)==int

        self._clusters=[]
        self._dataset=ds
        if seed_inds is None:
            seed_inds = random.sample(range(ds.getSize()), k)

        for x in range(k):
            a = Cluster(ds,ds.getPoint(seed_inds[x]))
            self._clusters.append(a)
        
    def getClusters(self):
        """Returns: The list of clusters in this object.
        
        This method returns the attribute _clusters directly.  Any changes
        made to this list will modify the set of clusters.
        """ 
        return self._clusters

    # Part B
    def _nearest_cluster(self, point):
        """Returns: Cluster nearest to point
    
        This method uses the distance method of each Cluster to compute the distance 
        between point and the cluster centroid. It returns the Cluster that is 
        the closest.
        
        Ties are broken in favor of clusters occurring earlier in the list of 
        self._clusters.
        
        Parameter point: the point to match
        Precondition: point is a list of numbers (int or float),
          len(point) = self._dataset.getDimension().
        """
        assert is_point(point) and len(point)==self._dataset.getDimension()
        
        leastdistance = self.getClusters()[0].distance(point)
        result = 0
        
        for x in range(len(self.getClusters())):
            if self.getClusters()[x].distance(point) < leastdistance:
                leastdistance = self.getClusters()[x].distance(point)
                result = x
                
        return self.getClusters()[result]
    
    def _partition(self):
        """Repartitions the dataset so each point is in exactly one Cluster.
        """        
        for x in range(len(self.getClusters())):
            self._clusters[x].clear()
            
        for x in range(self._dataset.getSize()):
            self._nearest_cluster(self._dataset.getContents()[x]).addIndex(x)
    
    # Part C
    def _update(self):
        """Returns:True if all centroids are unchanged after an update; False otherwise.
        
        This method first updates the centroids of all clusters'.  When it is done, it
        checks whether any of them have changed. It then returns the appropriate value.
        """
        
        result = True
        for i in range(len(self.getClusters())):
            if self.getClusters()[i].updateCentroid(): 
                pass
            else:
                result = False
        return result

    def step(self):
        """Returns: True if the algorithm converges after one step; False otherwise.
        
        This method performs one cycle of the k-means algorithm. It then checks if
        the algorithm has converged and returns True or False
        """
        self._partition()
        return not self._update()
    
    # Part D
    def run(self, maxstep):
        """Continues clustering until either it converges or reaches maxstep steps.
        
        The stopping condition (convergence, maxsteps) is whichever comes first.
        
        Precondition maxstep: Maximum number of steps before giving up
        Precondition: maxstep is int >= 0.
        """    
        assert isinstance(maxstep, int) and maxstep >= 0
        
        x = 0
        converge = False
        while x < maxstep and converge == False:
            converge = not self.step()            
            x = x + 1        
        
    
    # PROVIDED METHODS: Do not modify!
    def __str__(self):
        """Returns: String representation of the centroid of this cluster."""
        return str(self._clusters)
    
    def __repr__(self):
        """Returns: Unambiguous representation of this cluster. """
        return str(self.__class__) + str(self)
