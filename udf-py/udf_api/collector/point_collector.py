# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from abc import ABCMeta, abstractmethod

from udf_api.type.binary import Binary


class PointCollector(metaclass=ABCMeta):
    """
    Used to collect time series data points generated by UDTF.transform(Row, PointCollector), UDTF.transform(RowWindow,
    PointCollector) or UDTF.terminate(PointCollector). Notice that one timestamp can not be put in the PointCollector
    more than once, or it may stop the calculation.
    """

    @abstractmethod
    def put_int(self, timestamp: int, value: int):
        """
        Collects an int data point with timestamp.

        Before calling this method, you need to ensure that the UDF output data type is set to Type.INT32 by calling
        UDTFConfigurations.setOutputDataType(Type) in UDTF.beforeStart(UDFParameters, UDTFConfigurations).
        """
        pass

    @abstractmethod
    def put_long(self, timestamp: int, value: int):
        """
        Collects a long data point with timestamp.

        Before calling this method, you need to ensure that the UDF output data type is set to Type.INT64 by calling
        UDTFConfigurations.setOutputDataType(Type) in UDTF.beforeStart(UDFParameters, UDTFConfigurations).
        """
        pass

    @abstractmethod
    def put_float(self, timestamp: int, value: float):
        """
        Collects a float data point with timestamp.

        Before calling this method, you need to ensure that the UDF output data type is set to Type.FLOAT by
        calling UDTFConfigurations.setOutputDataType(Type) in UDTF.beforeStart(UDFParameters, UDTFConfigurations).
        """
        pass

    @abstractmethod
    def put_double(self, timestamp: int, value: float):
        """
        Collects a double data point with timestamp.

        Before calling this method, you need to ensure that the UDF output data type is set to Type.DOUBLE by
        calling UDTFConfigurations.setOutputDataType(Type) in UDTF.beforeStart(UDFParameters, UDTFConfigurations).
        """
        pass

    @abstractmethod
    def put_boolean(self, timestamp: int, value: bool):
        """
        Collects a boolean data point with timestamp.

        Before calling this method, you need to ensure that the UDF output data type is set to Type.BOOLEAN by calling
        UDTFConfigurations.setOutputDataType(Type) in UDTF.beforeStart(UDFParameters, UDTFConfigurations).
        """
        pass

    @abstractmethod
    def put_binary(self, timestamp: int, value: Binary):
        """
        Collects a Binary data point with timestamp.

        Before calling this method, you need to ensure that the UDF output data type is set to Type.TEXT by calling
        UDTFConfigurations.setOutputDataType(Type) in UDTF.beforeStart(UDFParameters, UDTFConfigurations).
        """
        pass

    @abstractmethod
    def put_string(self, timestamp: int, value: str):
        """
        Collects a String data point with timestamp.

        Before calling this method, you need to ensure that the UDF output data type is set to Type.TEXT by calling
        UDTFConfigurations.setOutputDataType(Type) in UDTF.beforeStart(UDFParameters, UDTFConfigurations).
        """
        pass
