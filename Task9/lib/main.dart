import 'package:flutter/material.dart';
import 'package:flutter_osm_plugin/flutter_osm_plugin.dart';
import 'dart:math';

import 'package:geolocator/geolocator.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
        useMaterial3: true,
      ),
      home: const MyHomePage(title: 'Flutter Demo Home Page'),
    );

  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  MapController controller = MapController.withUserPosition(
      trackUserLocation: UserTrackingOption(
        enableTracking: true,
        // unFollowUser: false,
      ));

  // var markerMap = <String,String>{
  // // GeoPoint? markedPoint;
  // // double distance = 0.0;
  //
  // };
  Future<void> drawRoads(
      GeoPoint userLocation, GeoPoint destination) async {
    final config = MultiRoadConfiguration(
      startPoint: userLocation,
      destinationPoint: destination,
      roadOptionConfiguration: MultiRoadOption(
        roadColor: Colors.blue,
      ),
    );

    await controller.drawMultipleRoad([config],
        commonRoadOption: MultiRoadOption(
          roadColor: Colors.red,
        ));
  }

  Map<String, GeoPoint> markerMap = {};
  double distance = 0.0;
  String totalDistance = "";
  String averageTime = "";


  @override
  void initState() {
    super.initState();


    WidgetsBinding.instance.addPostFrameCallback((_) {
      controller.listenerMapSingleTapping.addListener(() async{
        //When tap on map, we will add new marker
        var position = controller.listenerMapSingleTapping.value;
        if(position!=null){
          await controller.addMarker(position,markerIcon: const MarkerIcon(
            icon: Icon(Icons.pin_drop,color: Colors.blue,size: 28,),
          ));
          var key = '${position!.latitude}_${position!.longitude}';
          markerMap[key] = markerMap.length.toString() as GeoPoint;
          // calculateDistance();
        }
      });
    });
  }
  // Future<void> calculateDistance() async {
  //   if (controller.currentLocation == null || markerMap.isEmpty) {
  //     setState(() {
  //       distance = 0.0;
  //     });
  //     return;
  //   }
  //
  //   final GeoPoint currentPosition = controller.currentLocation as GeoPoint;
  //   final List<GeoPoint> markedPoints = markerMap.values.toList();
  //
  //   if (markedPoints.isNotEmpty) {
  //     double distanceInMeters = await distance2point(
  //       currentPosition,
  //       markedPoints.last,
  //     );
  //
  //     setState(() {
  //       distance = distanceInMeters / 1000.0;
  //       return;// Convert meters to kilometers
  //     });
  //
  //     print('Distance in meters: $distanceInMeters'); // Print the distance in meters
  //   } else {
  //     setState(() {
  //       distance = 0.0;
  //     });
  //   }
  // }

  // void calculateDistance() async{
  //   if (controller.currentLocation == null || markerMap.isEmpty) {
  //     setState(() {
  //       distance = 90.0;
  //     });
  //     return;
  //   }
  //
  //   final GeoPoint currentPosition = controller.currentLocation as GeoPoint;
  //   final List<GeoPoint> markedPoints = markerMap.keys.map((key) {
  //     final List<String> parts = key.split('_');
  //     final double latitude = double.parse(parts[0]);
  //     final double longitude = double.parse(parts[1]);
  //     return GeoPoint(latitude: latitude, longitude: longitude);
  //   }).toList();
  //
  //   if (markedPoints.isNotEmpty) {
  //     final double distanceInKm = _calculateDistanceBetween(
  //       currentPosition.latitude,
  //       currentPosition.longitude,
  //       markedPoints.last.latitude,
  //       markedPoints.last.longitude,
  //     );
  //
  //     setState(() {
  //       distance = distanceInKm;
  //     });
  //   } else {
  //     setState(() {
  //       distance = 90.0;
  //     });
  //   }
  // }

  double _calculateDistanceBetween(
      double lat1, double lon1, double lat2, double lon2) {
    const double earthRadius = 6371; // Radius of the Earth in kilometers

    final double dLat = _radians(lat2 - lat1);
    final double dLon = _radians(lon2 - lon1);

    final double a = sin(dLat / 2) * sin(dLat / 2) +
        cos(_radians(lat1)) *
            cos(_radians(lat2)) *
            sin(dLon / 2) *
            sin(dLon / 2);

    final double c = 2 * atan2(sqrt(a), sqrt(1 - a));

    return earthRadius * c;
  }

  double _radians(double degree) {
    return degree * (pi / 180);
  }

  @override
  void dispose() {
    super.dispose();
    controller.dispose();
  }
  // double calculateDistance(GeoPoint point1, GeoPoint point2) {
  //   const double radiusOfEarth = 6371.0; // Earth's radius in kilometers
  //   final lat1Radians = radians(point1.latitude);
  //   final lon1Radians = radians(point1.longitude);
  //   final lat2Radians = radians(point2.latitude);
  //   final lon2Radians = radians(point2.longitude);
  //
  //   final dlon = lon2Radians - lon1Radians;
  //   final dlat = lat2Radians - lat1Radians;
  //   final a = pow(sin(dlat / 2), 2) +
  //       cos(lat1Radians) * cos(lat2Radians) * pow(sin(dlon / 2), 2);
  //   final c = 2 * atan2(sqrt(a), sqrt(1 - a));
  //   return radiusOfEarth * c;
  // }
  // void onMarkerClicked(GeoPoint tappedPoint) {
  //   showModalBottomSheet(
  //       context: context,
  //       builder: (context) {
  //     final markerKey = '${tappedPoint.latitude}_${tappedPoint.longitude}';
  //     final marker = markerMap[markerKey];
  //     if (marker != null) {
  //       var centerPoint;
  //       final calculatedDistance = calculateDistance(
  //         controller.centerPoint,
  //         marker,
  //       );
  //       return Card(
  //         child: Column(
  //           children: [
  //             ListTile(
  //               title: Text('Marker clicked at:'),
  //               subtitle: Text(
  //                 'Latitude: ${tappedPoint.latitude}, Longitude: ${tappedPoint.longitude}',
  //               ),
  //             ),
  //             ListTile(
  //               title: Text('Distance to Marker:'),
  //               subtitle: Text(
  //                 'Distance: ${calculatedDistance.toStringAsFixed(2)} km',
  //               ),
  //             ),
  //           ],
  //         ),
  //       );
  //     } else {
  //       return Card(
  //         child: ListTile(
  //           title: Text('Marker clicked at:'),
  //           subtitle: Text(
  //             'Latitude: ${tappedPoint.latitude}, Longitude: ${tappedPoint.longitude}',
  //           ),
  //         ),
  //       );
  //     }
  //       },
  //   );
  // }
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: OSMFlutter(
          controller: controller,
          osmOption: OSMOption(
            userTrackingOption: UserTrackingOption(
              enableTracking: true,
              unFollowUser: false,
            ),
            zoomOption: ZoomOption(
              initZoom: 8,
              minZoomLevel: 3,
              maxZoomLevel: 19,
              stepZoom: 1.0,
            ),
            // androidHotReloadSupport: true;
            userLocationMarker: UserLocationMaker(
              personMarker: MarkerIcon(
                icon: Icon(
                  Icons.location_history_rounded,
                  color: Colors.black,
                  size: 48,
                ),
              ),
              directionArrowMarker: MarkerIcon(
                icon: Icon(
                  Icons.double_arrow,
                  size: 48,
                ),
              ),
            ),
            roadConfiguration: RoadOption(
              roadColor: Colors.yellowAccent,
            ),
            markerOption: MarkerOption(
              defaultMarker: MarkerIcon(
                icon: Icon(
                  Icons.person_pin_circle,
                  color: Colors.black,
                  size: 48,
                ),
              ),
            ),),
          onGeoPointClicked: (geoPoint) async{
            Position userLocation = await Geolocator.getCurrentPosition();
            GeoPoint userGeoPoint = GeoPoint(
                latitude: userLocation.latitude,
                longitude: userLocation.longitude);
            if (geoPoint != null) {
              double distanceInMeters = await distance2point(userGeoPoint, geoPoint);
              double speedInKm = 65.0;
              double totalDistanceKm = distanceInMeters / 1000;
              double averageTimeInHours = totalDistanceKm / speedInKm;
              double averageTimeInSeconds = averageTimeInHours * 60 * 60;

              setState(() {
                totalDistance = "${totalDistanceKm.toStringAsFixed(2)} km";
                averageTime = "${(averageTimeInSeconds / 60).toStringAsFixed(1)} minutes";

                // routeCard = createRouteCard(totalDistance, averageTime);
              });
    await drawRoads(userGeoPoint, geoPoint);
              showModalBottomSheet(
                context: context,
                builder: (context) {
                  return Card(
                    child: Column(
                      mainAxisSize: MainAxisSize.min,
                      children: <Widget>[

                        ListTile(
                          title: Text('Marker clicked at:'),
                          subtitle: Text(
                            'Latitude: ${geoPoint.latitude}, Longitude: ${geoPoint.longitude}',
                          ),
                        ),
                        ListTile(
                          title: Text("Total Distance: $totalDistance"),
                          subtitle: Text("Average Time: $averageTime"),
                          // subtitle: Text('${distance.toStringAsFixed(2)} km'),
                        ),

                      ],
                    ),
                  );
                },
              );
            }}
      ),);}

  double radians(double degrees) {
    return degrees * (pi / 180);
  }
}