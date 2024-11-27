import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HttpClientModule } from '@angular/common/http';
import { NamesComponent } from './names/names.component';
import { DataService } from './services/data.service';
import { DataComponent } from './data/data.component';
import { PollComponent } from './poll/poll.component';

@NgModule({
  declarations: [			
    AppComponent,
      NamesComponent,
      DataComponent,
      PollComponent
   ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [DataService],
  bootstrap: [AppComponent]
})
export class AppModule { }
