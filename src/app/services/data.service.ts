import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, interval, switchMap } from 'rxjs';

@Injectable()
export class DataService {

constructor(private http:HttpClient) { }

getData():Observable<any> {
    return interval(2000).pipe(
        switchMap(() => this.http.get('/assets/data.json'))
    );
}
}
